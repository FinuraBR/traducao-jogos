import json
import os
import glob

# --- CONFIGURAÇÕES ---
caminho_do_projeto = os.path.dirname(os.path.abspath(__file__))

# Precisamos do arquivo ORIGINAL para usar como molde (template)
arquivo_template = os.path.join(caminho_do_projeto, 'Data_S01_M01_DialogScript.json') 

# Pasta onde estão os JSONs traduzidos e verificados pela IA (que agora são listas simples)
pasta_traduzida = os.path.join(caminho_do_projeto, '3_partes_verificadas')

# Nome do arquivo final traduzido
arquivo_final = os.path.join(caminho_do_projeto, 'json_PTBR.json')

def juntar_json_v2():
    # 1. Carrega o arquivo original para pegar toda a estrutura técnica (metadados)
    if not os.path.exists(arquivo_template):
        print(f"❌ ERRO: Arquivo original '{arquivo_template}' não encontrado para usar como molde!")
        return

    with open(arquivo_template, 'r', encoding='utf-8') as f:
        dados_finais = json.load(f)
    
    # 2. Localiza todos os arquivos de partes traduzidas
    arquivos_partes = sorted(glob.glob(os.path.join(pasta_traduzida, 'parte_*.json')))

    if not arquivos_partes:
        print(f"❌ ERRO: Nenhum arquivo JSON encontrado em '{pasta_traduzida}'!")
        return

    print(f"📦 Juntando {len(arquivos_partes)} arquivos traduzidos...")

    # Criamos uma lista vazia onde vamos jogar todos os itens traduzidos
    lista_mestra_traduzida = []

    # 3. Percorre cada parte e adiciona os itens na nossa lista mestra
    for nome_arquivo in arquivos_partes:
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                itens_da_parte = json.load(f)
                
                # Como a parte agora é uma lista direta [], apenas estendemos a lista mestra
                if isinstance(itens_da_parte, list):
                    lista_mestra_traduzida.extend(itens_da_parte)
                else:
                    print(f"⚠️ AVISO: {nome_arquivo} não parece ser uma lista. Verifique a tradução da IA.")
                
        except Exception as e:
            print(f"❌ Erro ao ler {nome_arquivo}: {e}")
            return

    # 4. Injeta a lista traduzida de volta na estrutura original (Exports -> Table -> Data)
    # Isso garante que o cabeçalho e o rodapé da engine fiquem intactos
    dados_finais['Exports'][0]['Table']['Data'] = lista_mestra_traduzida

    # 5. Salva o arquivo final pronto para o UAssetGUI
    with open(arquivo_final, 'w', encoding='utf-8') as f_out:
        # indent=2 ajuda a manter a organização, mas o UAssetGUI lê mesmo sem isso
        json.dump(dados_finais, f_out, indent=2, ensure_ascii=False)

    print(f"\n🚀 SUCESSO! Arquivo completo criado: {arquivo_final}")
    print(f"Total de itens processados: {len(lista_mestra_traduzida)}")
    print("Agora você pode abrir o UAssetGUI e importar este JSON.")

if __name__ == '__main__':
    juntar_json_v2()