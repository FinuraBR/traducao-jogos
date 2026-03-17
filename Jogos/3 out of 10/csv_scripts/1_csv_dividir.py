"""
Script de Divisão de Arquivos para Tradução por IA.
Objetivo: Pegar um arquivo CSV grande (ex: E05.locres.csv) e dividi-lo em 
vários arquivos menores. Isso é necessário para evitar que o contexto da IA 
seja excedido (evita erros de corte de texto ou esquecimento de instruções).
"""

import os
import csv
import io

# --- CONFIGURAÇÕES ---
# Define o caminho do diretório onde o script está rodando
caminho_do_projeto = os.path.dirname(os.path.abspath(__file__))
# Localização do arquivo de entrada e da pasta onde as partes serão geradas
arquivo_original = os.path.join(caminho_do_projeto, 'E05.locres.csv')
pasta_saida = os.path.join(caminho_do_projeto, '1_partes_para_traduzir')

# LIMITE PARA IA (DeepSeek/Ollama/API Cloud)
# Definimos 8000 caracteres como margem de segurança. 
# Isso garante que a IA consiga ler o prompt do sistema + os dados + 
# ainda ter espaço para a resposta sem atingir o limite de tokens.
LIMITE_CARACTERES_POR_ARQUIVO = 8000 

def dividir_csv_inteligente():
    """
    Função principal que lê o arquivo CSV, calcula o tamanho de cada linha
    e agrupa em arquivos menores sem quebrar o formato CSV.
    """
    # Garante que a pasta de destino exista
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    print(f"Lendo {arquivo_original}...")

    try:
        # Abre o arquivo original para leitura
        with open(arquivo_original, 'r', encoding='utf-8', newline='') as f:
            # Usamos o csv.DictReader para manipular colunas como dicionários (fácil acesso)
            leitor = csv.DictReader(f)
            cabecalho = leitor.fieldnames
            # Carrega todas as linhas na memória (ideal para arquivos de tamanho médio)
            linhas_data = list(leitor)
    except Exception as e:
        print(f"❌ ERRO ao ler arquivo: {e}")
        return

    if not linhas_data:
        print("O arquivo está vazio!")
        return

    print(f"\n✅ Encontrados {len(linhas_data)} registros. Dividindo por tamanho de texto...")

    buffer_linhas = []       # Armazena as linhas que estão sendo agrupadas
    tamanho_atual_buffer = 0 # Contador para monitorar o tamanho total do buffer
    contador_arquivos = 1    # Numeração do arquivo gerado

    for row in linhas_data:
        # Simula a escrita da linha para um buffer de memória (io.StringIO)
        # Isso nos permite medir exatamente quantos caracteres essa linha ocupará no arquivo final
        output = io.StringIO()
        escritor_temp = csv.DictWriter(output, fieldnames=cabecalho)
        escritor_temp.writerow(row)
        linha_texto = output.getvalue()
        
        tamanho_linha = len(linha_texto)

        # Lógica de agrupamento:
        # Se adicionar esta nova linha estourar o limite permitido, salvamos o que temos
        # no buffer e começamos um novo arquivo.
        if (tamanho_atual_buffer + tamanho_linha) > LIMITE_CARACTERES_POR_ARQUIVO and buffer_linhas:
            salvar_parte_csv(cabecalho, buffer_linhas, contador_arquivos)
            contador_arquivos += 1
            buffer_linhas = []        # Reseta o buffer
            tamanho_atual_buffer = 0  # Reseta o contador de tamanho

        # Adiciona a linha atual ao buffer
        buffer_linhas.append(row)
        tamanho_atual_buffer += tamanho_linha

    # Salva as linhas que restaram no buffer após terminar o loop
    if buffer_linhas:
        salvar_parte_csv(cabecalho, buffer_linhas, contador_arquivos)

    print(f"\n🚀 Sucesso! {len(linhas_data)} entradas divididas em {contador_arquivos} arquivos.\n")
    print(f"Pasta: {pasta_saida}")

def salvar_parte_csv(cabecalho, dados, numero_parte):
    """
    Função auxiliar para gravar os dados em um novo arquivo CSV.
    Usa o formato parte_XXX.csv para manter a ordem alfabética/numérica correta.
    """
    # Define o nome do arquivo com padding de 3 dígitos (ex: 001, 002)
    nome_arquivo = os.path.join(pasta_saida, f'parte_{numero_parte:03d}.csv')
    
    with open(nome_arquivo, 'w', encoding='utf-8', newline='') as f_out:
        # Cria o escritor CSV e escreve o cabeçalho original
        escritor = csv.DictWriter(f_out, fieldnames=cabecalho)
        escritor.writeheader() 
        # Escreve todas as linhas agrupadas
        escritor.writerows(dados)
    
    print(f"  -> Gerado: parte_{numero_parte:03d}.csv ({len(dados)} entradas)")

if __name__ == '__main__':
    # Executa a lógica de divisão
    dividir_csv_inteligente()