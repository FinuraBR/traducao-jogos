import json
import os

caminho_do_projeto = os.path.dirname(os.path.abspath(__file__))

# 1. O arquivo original perfeito (que você extraiu do FModel/UAssetGUI)
arquivo_original = os.path.join(caminho_do_projeto, 'Data_S01_M01_DialogScript.json') 

# 2. O arquivo com as traduções feitas pela IA
arquivo_traduzido = os.path.join(caminho_do_projeto, 'json_PTBR.json')

# 3. O arquivo final blindado que vamos gerar
arquivo_seguro = os.path.join(caminho_do_projeto, 'SEGURO.json')

def resgatar_traducao():
    print("📥 Carregando arquivos...")
    with open(arquivo_original, 'r', encoding='utf-8') as f:
        dados_originais = json.load(f)
    
    with open(arquivo_traduzido, 'r', encoding='utf-8') as f:
        dados_traduzidos = json.load(f)

    print("💉 Injetando traduções cirurgicamente...")
    
    # Função que viaja por todo o JSON e só copia o texto correto
    def substituir_textos(original, traduzido):
        if isinstance(original, dict) and isinstance(traduzido, dict):
            for chave in original:
                # SE a chave for o texto do jogo, nós substituímos
                if chave == "CultureInvariantString" or chave == "LocalizedString":
                    if traduzido.get(chave) is not None:
                        original[chave] = traduzido[chave]
                # Se for qualquer outra chave de código, nós apenas entramos nela (ignorando a tradução da IA)
                elif chave in traduzido:
                    substituir_textos(original[chave], traduzido[chave])
                    
        elif isinstance(original, list) and isinstance(traduzido, list):
            # Garante que não vai dar erro se a IA tiver apagado alguma linha
            limite = min(len(original), len(traduzido))
            for i in range(limite):
                substituir_textos(original[i], traduzido[i])

    # Aplicamos a cirurgia apenas na parte dos Dados
    lista_original = dados_originais['Exports'][0]['Table']['Data']
    lista_traduzida = dados_traduzidos['Exports'][0]['Table']['Data']

    substituir_textos(lista_original, lista_traduzida)

    print("💾 Salvando o arquivo blindado...")
    with open(arquivo_seguro, 'w', encoding='utf-8') as f:
        json.dump(dados_originais, f, indent=2, ensure_ascii=False)

    print(f"✅ SUCESSO! O arquivo perfeito foi gerado:")
    print(f"-> {arquivo_seguro}")

if __name__ == '__main__':
    resgatar_traducao()