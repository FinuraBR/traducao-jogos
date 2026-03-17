"""
Script de União (Merge) de Arquivos CSV.
Objetivo: Consolida todas as partes traduzidas individuais (parte_001.csv, 
parte_002.csv, etc.) em um único arquivo mestre (csv_PTBR.locres.csv).
"""

import os
import glob

# --- CONFIGURAÇÕES ---
# Define o diretório base para que o script funcione independentemente de onde for executado
caminho_do_projeto = os.path.dirname(os.path.abspath(__file__))

# Pasta onde estão as partes traduzidas pela IA
pasta_arquivos_traduzidos = os.path.join(caminho_do_projeto, '2_partes_traduzidas')

# Nome do arquivo final que conterá toda a tradução unida
arquivo_final = os.path.join(caminho_do_projeto, 'csv_PTBR.locres.csv')

def juntar_csv_seguro():
    """
    Lê todos os arquivos CSV na pasta de entrada e os combina em um único arquivo,
    garantindo que o cabeçalho seja escrito apenas uma vez.
    """
    
    # glob.glob encontra os arquivos, sorted() garante a ordem (parte_001 antes de parte_002)
    # Sem o sorted(), a ordem poderia ser aleatória dependendo do sistema operacional.
    arquivos_partes = sorted(glob.glob(os.path.join(pasta_arquivos_traduzidos, '*.csv')))

    if not arquivos_partes:
        print(f"❌ Nenhum arquivo CSV encontrado em: {pasta_arquivos_traduzidos}")
        return

    print(f"--- INICIANDO UNIÃO DE {len(arquivos_partes)} ARQUIVOS ---")
    
    linhas_totais = 0
    primeiro_arquivo = True # Flag para controlar a escrita do cabeçalho

    # Abre o arquivo de saída em modo de escrita ('w')
    with open(arquivo_final, 'w', encoding='utf-8') as f_out:
        for arquivo in arquivos_partes:
            nome_simples = os.path.basename(arquivo)
            
            with open(arquivo, 'r', encoding='utf-8') as f_in:
                # Lê todas as linhas do arquivo atual na memória
                linhas = f_in.readlines()
                
                # Proteção contra arquivos corrompidos ou vazios
                if not linhas:
                    print(f"⚠️ Aviso: O arquivo {nome_simples} está vazio. Pulando...")
                    continue

                # LÓGICA DE CABEÇALHO:
                # Se for o primeiro arquivo, escrevemos o cabeçalho (linha 0)
                if primeiro_arquivo:
                    f_out.write(linhas[0])
                    primeiro_arquivo = False # Desativa flag para nunca mais escrever o cabeçalho
                    
                    # Se o arquivo só tiver o cabeçalho (sem dados), pula para o próximo
                    if len(linhas) < 2: 
                        continue
                
                # LÓGICA DE DADOS:
                # Pegamos da linha 1 em diante (linhas[1:]), ignorando o cabeçalho das partes seguintes
                dados_traduzidos = linhas[1:]
                
                for linha in dados_traduzidos:
                    conteudo = linha.strip() # Remove espaços extras e quebras de linha no fim
                    if conteudo:  # Só escreve se a linha tiver algum conteúdo relevante
                        # Escreve a linha e adiciona uma quebra de linha manual para padronizar
                        f_out.write(conteudo + '\n')
                        linhas_totais += 1
            
            print(f"✅ Integrado: {nome_simples}")

    print("-" * 30)
    print(f"🚀 SUCESSO! Arquivo final gerado: {os.path.basename(arquivo_final)}")
    print(f"📊 Total de linhas de tradução unidas: {linhas_totais}")
    print("DICA: Compare este número com o total de linhas do arquivo original antes da divisão.")

if __name__ == '__main__':
    juntar_csv_seguro()