import os
import ollama
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor

# --- CONFIGURAÇÃO DE PERFORMANCE ---
MAX_WORKERS = 3       # 3 para modelo cloud | Quantos arquivos revisar ao mesmo tempo
DELAY_START = 3.0     # 3.0 para modelo cloud | Segundos entre o início de cada revisão (evita gargalo)

# --- CONFIGURAÇÃO DE PASTAS ---
caminho_do_projeto = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(caminho_do_projeto, "2_partes_traduzidas")  
output_folder = os.path.join(caminho_do_projeto, "3_partes_verificadas")   

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- PROMPT DE LQA PARA JSON ---
prompt_sistema = """YOU ARE A SENIOR LOCALIZATION QA SPECIALIST (LQA).
Your ONLY output is the corrected and finalized JSON content.

Task:
Review and FIX the provided JSON file containing translations for a game.

LQA Checklist:
1. LOCALIZATION: Ensure the text within "CultureInvariantString" is natural and idiomatic PT-BR.
2. TAGS & VARIABLES: Verify that ALL tags like <cf>, {0}, %s, \\n are identical to the source.
3. JSON SYNTAX: If the text has double quotes, you MUST escape them (e.g., \\").

Technical Rules:
- Format: VALID JSON (UAssetAPI structure).
- DO NOT modify keys like "$type", "Name", "Namespace", etc.
- NO markdown, NO conversation, NO notes.

START PROCESSING NOW."""

def validar_e_limpar_json(texto_resposta):
    """Remove lixo da IA e garante que o JSON seja válido antes de retornar o objeto."""
    if not texto_resposta or not texto_resposta.strip():
        return None
    # Remove markdown
    texto_limpo = re.sub(r"```(?:json|text)?\n?", "", texto_resposta)
    texto_limpo = texto_limpo.replace("```", "").strip()
    try:
        objeto_valido = json.loads(texto_limpo)
        return objeto_valido
    except:
        return None

def processar_arquivo_lqa(nome_arquivo):
    """Função para processar um único arquivo LQA (chamada pelas threads)"""
    caminho_in = os.path.join(input_folder, nome_arquivo)
    caminho_out = os.path.join(output_folder, nome_arquivo)
    
    # Pula se já existir
    if os.path.exists(caminho_out):
        return

    tentativas_maximas = 3
    prefixo = f"({nome_arquivo})"

    for tentativa in range(1, tentativas_maximas + 1):
        try:
            with open(caminho_in, 'r', encoding='utf-8') as f:
                conteudo_json = f.read()

            print(f"Revisando {prefixo} | Tentativa {tentativa}", flush=True)

            response = ollama.generate(
                model='gpt-oss:120b-cloud', 
                #model='deepseek-v3.1:671b-cloud',
                system=prompt_sistema,
                prompt=f"{conteudo_json}",
                format='json', 
                stream=False,
                options={
                    "temperature": 0.3,
                    "num_ctx": 16384,
                    "top_p": 0.9,
                    "num_predict": 8192
                }
            )
            
            json_objeto = validar_e_limpar_json(response.get('response', ''))
            
            if json_objeto:
                with open(caminho_out, 'w', encoding='utf-8') as f:
                    json.dump(json_objeto, f, indent=2, ensure_ascii=False)
                print(f"✅ {prefixo} Verificado", flush=True)
                return
            else:
                if tentativa < tentativas_maximas:
                    time.sleep(3)
                else:
                    print(f"❌ {prefixo} Falha na validação após {tentativas_maximas} tentativas.", flush=True)

        except Exception as e:
            print(f"❌ {prefixo} Erro Geral: {e}", flush=True)
            break

# --- EXECUÇÃO TURBO ---
if __name__ == '__main__':
    arquivos = sorted([f for f in os.listdir(input_folder) if f.endswith(".json")])
    
    print(f"--- INICIANDO LQA TURBO ({MAX_WORKERS} WORKERS) ---", flush=True)
    print(f"Arquivos para processar: {len(arquivos)}\n", flush=True)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for nome_arquivo in arquivos:
            # Verifica existência antes de agendar a thread para economizar tempo
            caminho_out = os.path.join(output_folder, nome_arquivo)
            if os.path.exists(caminho_out):
                print(f"⏩ {nome_arquivo} já existe", flush=True)
                continue
            
            executor.submit(processar_arquivo_lqa, nome_arquivo)
            time.sleep(DELAY_START)

    print("\n--- TODO O PROCESSO DE LQA FOI FINALIZADO! ---")