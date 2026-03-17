"""
Script de Tradução Automática de CSV via IA (Cloud/Cloud API).
Objetivo: Processar arquivos CSV em lote, enviando-os para uma IA (via Puter),
validando a estrutura de saída e salvando os resultados, com mecanismos de 
retry (reenvio) e timeout.
"""

import os
import re
import sys
import time
import subprocess
import threading

# Ajusta o path do sistema para permitir importações de diretórios acima (arquitetura de pastas)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- CONFIGURAÇÕES GLOBAIS ---
from config import (
    MODELO_EXTERNO,
    API_KEY,
    TIMEOUT_LIMITE,
    MAX_TENTATIVAS
)

# Validação de dependências externas
try:
    from puter import ChatCompletion  
except ImportError:
    print("❌ Erro: A biblioteca 'puter' não está instalada.")
    sys.exit(1)

# Prompt de sistema: Define o comportamento da IA.
# É fundamental que a IA não saia do formato CSV solicitado, 
# por isso a proibição de markdown e explicações.
DEFAULT_SYSTEM_PROMPT = """Natural Game Localizer (EN -> PT-BR).
Task: Translation/localization 'Translation' column based on 'source'. Use surrounding items for context.
Rule 1: Keep 'key' identical.
Rule 2: Use quotes " " for translations with commas (,).
Rule 3: No talk or markdown.
Format: key,source,Translation
Output: Valid CSV only"""

def limpar_resposta_ia(texto_bruto):
    """
    Remove "ruídos" da IA (tags de pensamento, blocos markdown) e tenta isolar
    apenas o conteúdo CSV válido.
    """
    if not texto_bruto: return ""
    texto_str = str(texto_bruto)
    
    # 1. Remove tags de raciocínio (ex: <think>...</think> comum em modelos modernos)
    texto_limpo = re.sub(r'<think>.*?</think>', '', texto_str, flags=re.DOTALL)
    
    # 2. Remove blocos de código Markdown (```csv ... ```)
    texto_limpo = re.sub(r'```(?:csv|text)?\n?', '', texto_limpo).replace('```', '').strip()
    
    # 3. Validação de estrutura: Garante que começa com o cabeçalho correto
    linhas = texto_limpo.split('\n')
    csv_linhas = []
    em_csv = False
    for linha in linhas:
        if linha.lower().startswith('key,source,translation'):
            em_csv = True
            csv_linhas.append(linha)
        elif em_csv and (linha.count(',') >= 2 or not linha.strip()):
            csv_linhas.append(linha)
        elif em_csv:
            break # Para se encontrar uma linha que não parece CSV
    return '\n'.join(csv_linhas) if csv_linhas else texto_limpo

def executar_chamada_ia(prompt_sistema, prompt_usuario, resultado_container):
    """
    Executa a chamada à API Puter em uma função separada para ser chamada por threads.
    """
    try:
        res = ChatCompletion.create(
            model=MODELO_EXTERNO,
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ],
            api_key=API_KEY
        )
        resultado_container['res'] = res
    except Exception as e:
        resultado_container['erro'] = e

def obter_traducao_com_timeout(csv_content):
    """
    Gerencia a execução da IA com timeout.
    Se a IA travar ou demorar demais, a thread é encerrada e tentamos novamente.
    """
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        print(f"📞 Chamando IA (Tentativa {tentativa}/{MAX_TENTATIVAS})...")
        
        container = {'res': None, 'erro': None}
        # Cria thread para permitir o timeout (join com timeout)
        t = threading.Thread(target=executar_chamada_ia, args=(DEFAULT_SYSTEM_PROMPT, csv_content, container))
        t.daemon = True
        t.start()
        
        t.join(timeout=TIMEOUT_LIMITE)
        
        # Se a thread ainda estiver viva após o timeout, falhou
        if t.is_alive():
            print(f"⏳ Tempo esgotado ({TIMEOUT_LIMITE}s)!")
            if tentativa < MAX_TENTATIVAS:
                print("🔄 Reenviando prompt agora...\n")
                time.sleep(1)
            continue

        if container['erro']:
            print(f"❌ Erro na API: {container['erro']}")
            if tentativa < MAX_TENTATIVAS: time.sleep(2)
            continue

        # Extração dos dados da resposta (padronização da API Puter)
        resposta = container['res']
        texto_final = ""
        
        if isinstance(resposta, dict):
            if not resposta.get('success', True):
                print(f"⚠️ Erro retornado: {resposta.get('error')}")
                continue
            
            res_obj = resposta.get('reesult') or resposta.get('result') or resposta
            if 'message' in res_obj:
                texto_final = res_obj['message']['content']
        else:
            texto_final = str(resposta)

        # Sanitiza a resposta antes de retornar
        resultado = limpar_resposta_ia(texto_final)
        if resultado:
            return resultado

    return None

def main():
    # Caminhos de entrada e saída
    input_folder = r"D:\EP1\csv_scripts\1_partes_para_traduzir"
    output_folder = r"D:\EP1\csv_scripts\2_partes_traduzidas"

    if not os.path.exists(output_folder): os.makedirs(output_folder)

    # Lista todos os arquivos da entrada
    todos_arquivos = sorted([f for f in os.listdir(input_folder) if f.endswith(".csv")])
    
    # Filtra apenas os que NÃO existem na saída (Idempotência: permite continuar de onde parou)
    arquivos_pendentes = [f for f in todos_arquivos if not os.path.exists(os.path.join(output_folder, f))]
    
    pulados = len(todos_arquivos) - len(arquivos_pendentes)
    if pulados > 0:
        print(f"\n⏩ {pulados} partes já traduzidas foram detectadas e serão ignoradas.")

    if not arquivos_pendentes:
        print("✨ Tudo pronto! Não há novas partes para processar.")
        return

    print(f"\n🚀 Iniciando Tradução Linear | {len(arquivos_pendentes)} arquivos restantes.\n")

    # Loop principal
    for filename in arquivos_pendentes:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        print(f"--- Processando Arquivo: {filename} ---")
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                conteudo = f.read()

            if not conteudo.strip(): continue

            # Chama a tradução
            traducao = obter_traducao_com_timeout(conteudo)

            if traducao:
                # Salva o resultado
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(traducao)
                print(f"✅ Arquivo salvo: {filename}\n")
                
                # Abre automaticamente o VS Code para revisão humana imediata
                subprocess.run(['code', output_path], shell=True)
            else:
                print(f"❌ Falha total no arquivo {filename} após {MAX_TENTATIVAS} tentativas.\n")

        except Exception as e:
            print(f"💥 Erro inesperado no arquivo {filename}: {e}\n")

    print("🏁 Workflow de tradução encerrado.")

if __name__ == '__main__':
    main()