import os
import subprocess
import ollama
import json
import time
from concurrent.futures import ThreadPoolExecutor

# --- CONFIGURAÇÃO DE PERFORMANCE ---
MAX_WORKERS = 3       # Quantos arquivos traduzir ao mesmo tempo
DELAY_START = 3.0     # Segundos de intervalo ao lançar cada nova thread (evita gargalo)

# --- CONFIGURAÇÃO DE PASTAS ---
caminho_do_projeto = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(caminho_do_projeto, "1_partes_para_traduzir")  
output_folder = os.path.join(caminho_do_projeto, "2_partes_traduzidas")   

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- PROMPT PARA JSON ---
prompt_sistema = """YOU ARE A SENIOR LOCALIZATION EXPERT (ENGLISH TO BRAZILIAN PORTUGUESE).
Your ONLY output is the processed JSON content.

Task:
Localize the text within "CultureInvariantString" into Brazilian Portuguese (pt-BR).

Localization Guidelines:
1. Provide a high-quality localization. Adapt the text to sound natural and idiomatic for the Brazilian audience, ensuring it flows well in Portuguese while maintaining the original intent.

Technical Rules:
1. Input is a UAssetAPI JSON structure. Output MUST be the exact same JSON format.
2. Localize ONLY the values of "CultureInvariantString".
3. DO NOT modify keys or technical fields ($type, Name, Namespace, etc.).
4. PRESERVE all tags and variables like <cf>, {0}, %s, \\n, \\r exactly as they appear.
5. Ensure valid JSON syntax. If the translation contains double quotes, you MUST escape them with a backslash (e.g. \\").

OUTPUT: Return ONLY the raw JSON. No explanations, no markdown blocks."""

def processar_arquivo(nome_arquivo):
    caminho_in = os.path.join(input_folder, nome_arquivo)
    caminho_out = os.path.join(output_folder, nome_arquivo)
    
    if os.path.exists(caminho_out):
        # MUDANÇA: Agora ele avisa que está pulando
        print(f"⏩ {nome_arquivo} já existe", flush=True)
        return

    tentativas_maximas = 3
    
    for tentativa in range(1, tentativas_maximas + 1):
        try:
            with open(caminho_in, 'r', encoding='utf-8') as f:
                dados_json = json.load(f)
                texto_para_ia = json.dumps(dados_json, ensure_ascii=False)

            prefixo = f"({nome_arquivo})"
            print(f"Iniciando {prefixo} | Tentativa {tentativa}")
            
            response = ollama.generate(
                model='gpt-oss:120b-cloud', 
                #model='deepseek-v3.1:671b-cloud', 
                system=prompt_sistema,
                prompt=texto_para_ia,
                format='json', 
                stream=False,
                options={
                    "temperature": 0.6,
                    "num_ctx": 16384,
                    "top_p": 0.95,
                    "num_predict": 8192
                }
            )

            res_raw = response.get('response', "").strip()
            if not res_raw:
                raise ValueError("Resposta vazia")

            json_traduzido = json.loads(res_raw)

            with open(caminho_out, 'w', encoding='utf-8') as f:
                json.dump(json_traduzido, f, indent=2, ensure_ascii=False)
                
            print(f"✅ {prefixo} Concluído")
            return f"{nome_arquivo}: OK"

        except (json.JSONDecodeError, ValueError) as e:
            if tentativa < tentativas_maximas:
                time.sleep(3) # Espera um pouco antes de tentar de novo
            else:
                print(f"❌ {nome_arquivo}: Falha após {tentativas_maximas} tentativas. (Erro JSON)")
        except Exception as e:
            print(f"❌ {nome_arquivo}: Erro Geral: {e}")
            break
    
    return f"{nome_arquivo}: FALHA"

# --- EXECUÇÃO MULTITHREAD ---
if __name__ == '__main__':
    arquivos = sorted([f for f in os.listdir(input_folder) if f.endswith(".json")])
    
    print(f"--- INICIANDO TRADUÇÃO TURBO ({MAX_WORKERS} WORKERS) ---", flush=True)
    print(f"Total de arquivos: {len(arquivos)}\n", flush=True)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for nome_arquivo in arquivos:
            # Verifica antes de mandar para a thread para não dar o delay à toa
            caminho_out = os.path.join(output_folder, nome_arquivo)
            if os.path.exists(caminho_out):
                print(f"⏩ {nome_arquivo} já existe", flush=True)
                continue # Pula para o próximo sem fazer o executor.submit e sem o sleep
            
            executor.submit(processar_arquivo, nome_arquivo)
            time.sleep(DELAY_START)

    print("\n--- TODO O PROCESSO TURBO FOI FINALIZADO!---\n---INICIANDO PROXIMA ETAPA EM 3 SEGUNDOS---")
    time.sleep(3)
    print()
    subprocess.run(["python", "3_json_verificar.py"])