"""
Script de Automação de Tradução via IA.
Responsável por:
1. Ler arquivos JSON da pasta de entrada.
2. Enviar para a IA (Local ou Cloud) com instruções estritas.
3. Validar se a IA manteve a integridade das tags técnicas.
4. Salvar os resultados e automatizar o workflow de revisão.
"""

import os
import json
import time
import re
import subprocess
import threading
import sys  # Importado para forçar a parada do script em erros críticos

# --- CONFIGURAÇÕES GLOBAIS ---
from config import (
    PASTA_PARTES_1,
    PASTA_PARTES_3,
    USA_EXTERNO, 
    MODELO_IA,
    MODELO_EXTERNO,
    API_KEY,
    TIMEOUT_LIMITE,
    MAX_TENTATIVAS
)

# Inicialização de dependências baseado na escolha (Local vs Cloud)
if USA_EXTERNO:
    from puter import ChatCompletion  
else:
    import ollama

input_folder = PASTA_PARTES_1
output_folder = PASTA_PARTES_3

# Garante que a pasta de destino exista
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- PROMPT REFINADO ---
# Define como a IA deve se comportar. O formato JSON é obrigatório.
prompt_sistema = """Natural Gamer Localizer (EN -> PT-BR).
Task: Translation/localization 't' values. Use surrounding items for context.
Rule 1: Keep 'p' keys identical.
Rule 2: No explanations, no markdown, no thinking tags.
Format: [{"p": "path", "t": "translation"}]
Output: Valid JSON array ONLY."""

def validar_integridade_tags(original, traduzido):
    """
    Verifica se a tradução manteve todas as variáveis técnicas (ex: {0}, %s, tags HTML).
    Isso evita que o jogo quebre por falta de variáveis no texto traduzido.
    """
    pattern = re.compile(r'\{.*?\}|<.*?>|%[sd]')
    tags_originais = pattern.findall(original)
    tags_traduzidas = pattern.findall(traduzido)
    # Compara a contagem e os tipos de tags encontrados
    return len(tags_originais) == len(tags_traduzidas)

def limpar_resposta_ia(texto_bruto):
    """
    Sanitiza a saída da IA:
    1. Remove blocos de raciocínio (<think>...</think>) comuns em modelos recentes.
    2. Extrai apenas o array JSON puro, ignorando explicações introdutórias ou finais.
    """
    if not texto_bruto: return ""
    texto_str = str(texto_bruto)
    # Remove tags de pensamento (DeepSeek/Ollama)
    texto_limpo = re.sub(r'<think>.*?</think>', '', texto_str, flags=re.DOTALL)
    try:
        # Tenta isolar o conteúdo entre colchetes []
        inicio = texto_limpo.find('[')
        fim = texto_limpo.rfind(']') + 1
        if inicio != -1 and fim != 0:
            return texto_limpo[inicio:fim].strip()
    except Exception:
        pass
    return texto_limpo.strip()

# --- FUNÇÕES DE CHAMADA COM ISOLAMENTO ---

def chamada_ia_thread(texto, container):
    """
    Executa a requisição à IA em uma thread separada.
    Isso permite que o script principal aplique um 'timeout', 
    evitando travamentos se a API demorar demais para responder.
    """
    try:
        if USA_EXTERNO:
            # Integração com API de Nuvem (Puter/OpenAI)
            resposta = ChatCompletion.create(
                model=MODELO_EXTERNO, 
                messages=[{"role": "system", "content": prompt_sistema}, {"role": "user", "content": texto}],
                api_key=API_KEY
            )
            
            texto_extraido = ""
            if isinstance(resposta, dict):
                # Verificação de erro de saldo/crédito na API
                if 'code' in resposta and resposta['code'] == 'insufficient_funds':
                    container['erro'] = f"FATAL: {resposta}"
                    return

                if not resposta.get('success', True):
                    container['erro'] = f"Erro API: {resposta.get('error')}"
                    return
                # Padronização de acesso aos dados da resposta
                res = resposta.get('reesult') or resposta.get('result') or resposta
                texto_extraido = res['message']['content'] if 'message' in res else str(res)
            else:
                texto_extraido = str(resposta)
            container['resultado'] = limpar_resposta_ia(texto_extraido)
            
        else:
            # Integração com Ollama (Local)
            response = ollama.generate(
                model=MODELO_IA, system=prompt_sistema, prompt=texto, format='json', stream=False
            )
            container['resultado'] = response.get('response', '').strip()
            
    except Exception as e:
        container['erro'] = str(e)

def obter_traducao_segura(texto_original):
    """
    Gerencia o ciclo de vida da requisição:
    - Executa a thread.
    - Monitora o timeout.
    - Implementa lógica de reenvio (retry) caso falhe.
    """
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        print(f"📞 Chamando IA (Tentativa {tentativa}/{MAX_TENTATIVAS})...")
        
        container = {'resultado': None, 'erro': None}
        t = threading.Thread(target=chamada_ia_thread, args=(texto_original, container))
        t.daemon = True
        t.start()
        
        # Espera pela resposta até o limite de tempo configurado
        t.join(timeout=TIMEOUT_LIMITE)
        
        if t.is_alive():
            print(f"⏳ Tempo esgotado ({TIMEOUT_LIMITE}s)!")
            if tentativa < MAX_TENTATIVAS:
                print("🔄 Reenviando prompt...")
            continue
            
        if container['erro']:
            erro_msg = str(container['erro'])
            print(f"❌ Erro na chamada: {erro_msg}")
            
            # --- PROTEÇÃO FINANCEIRA ---
            # Se não há saldo ou API inacessível, interrompe o script para evitar loop de erros
            if "insufficient_funds" in erro_msg or "402" in erro_msg:
                sys.exit(1) 
            # ---------------------------

            if tentativa < MAX_TENTATIVAS: time.sleep(1)
            continue
            
        if container['resultado']:
            return container['resultado']
            
    return None

# --- PROCESSAMENTO PRINCIPAL ---

def processar_arquivo(nome_arquivo):
    """
    Controla o fluxo de um único arquivo: 
    Carregar -> Traduzir -> Validar -> Salvar.
    """
    caminho_in = os.path.join(input_folder, nome_arquivo)
    caminho_out = os.path.join(output_folder, nome_arquivo)
    
    # Se já existir arquivo traduzido, pula para economizar recursos
    if os.path.exists(caminho_out):
        return {"status": "pulado"}

    try:
        with open(caminho_in, 'r', encoding='utf-8') as f:
            dados_originais = json.load(f)
        
        qtd_esperada = len(dados_originais)
        print(f"🚀 {nome_arquivo} - Iniciando tradução de {qtd_esperada} itens")
        
        # Solicita a tradução via IA
        resposta_raw = obter_traducao_segura(json.dumps(dados_originais, ensure_ascii=False))
        
        if not resposta_raw: 
            raise ValueError("Falha definitiva: IA não respondeu ou deu erro")

        # Converte resposta da IA para JSON
        dados_traduzidos = json.loads(resposta_raw)
        
        # Ajuste caso a IA encapsule a resposta em uma chave extra
        if isinstance(dados_traduzidos, dict):
            for key in dados_traduzidos:
                if isinstance(dados_traduzidos[key], list):
                    dados_traduzidos = dados_traduzidos[key]
                    break

        # Validação estrutural: Garante que a IA não removeu itens
        if not isinstance(dados_traduzidos, list) or len(dados_traduzidos) != qtd_esperada:
            raise ValueError(f"Contagem incorreta! Esperado {qtd_esperada}, recebeu {len(dados_traduzidos) if isinstance(dados_traduzidos, list) else '?'}")

        # Validação de conteúdo: Verifica cada tag nas frases
        for i in range(qtd_esperada):
            if not validar_integridade_tags(dados_originais[i]['t'], dados_traduzidos[i]['t']):
                raise ValueError(f"Tags corrompidas na linha {i}")
            
        with open(caminho_out, 'w', encoding='utf-8') as f:
            json.dump(dados_traduzidos, f, indent=2, ensure_ascii=False)

        print(f"✅ {nome_arquivo} - Sucesso!")
        return {"status": "sucesso", "caminho": caminho_out}
    
    except Exception as e:
        print(f"💥 Erro fatal em {nome_arquivo}: {e}")
        return {"status": "falha"}

def executar_traducao_linear():
    """
    Função controladora que percorre todos os arquivos disponíveis e orquestra
    a tradução sequencial.
    """
    arquivos = sorted([f for f in os.listdir(input_folder) if f.endswith(".json")])
    arquivos_para_processar = [f for f in arquivos if not os.path.exists(os.path.join(output_folder, f))]
    
    if not arquivos_para_processar: 
        print("✅ Tudo traduzido.")
        return
    
    modo = "PUTER (CLOUD)" if USA_EXTERNO else "OLLAMA (LOCAL)"
    print(f"\n🤖 [INICIANDO TRADUÇÃO LINEAR: {modo} - {len(arquivos_para_processar)} ARQUIVOS]\n")

    for arq in arquivos_para_processar:
        time.sleep(1) # Pausa de segurança entre arquivos
        resultado = processar_arquivo(arq)
        
        # Se teve sucesso, abre o arquivo para revisão humana imediata
        if resultado["status"] == "sucesso":
            subprocess.run(['code', resultado["caminho"]], shell=True)
        
        # Se falhou, para o script para evitar gastos desnecessários ou corrupção
        elif resultado["status"] == "falha":
            print(f"🛑 Ocorreu um erro crítico. Parando automação para revisão.")
            break

def main():
    executar_traducao_linear()
    print("\n🏁 Workflow finalizado.")

if __name__ == '__main__':
    main()