import json
import os

caminho_do_projeto = os.path.dirname(os.path.abspath(__file__))
arquivo_original = os.path.join(caminho_do_projeto, 'Data_S01_M01_DialogScript.json') 
pasta_saida = os.path.join(caminho_do_projeto, '1_partes_para_traduzir')

# Diminuímos para 5000 caracteres de TEXTO PURO para garantir que o DeepSeek responda rápido
LIMITE_CARACTERES = 5000 

def dividir_json_v2():
    if not os.path.exists(pasta_saida): os.makedirs(pasta_saida)

    with open(arquivo_original, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    # Pegamos apenas a lista de dados, sem o cabeçalho e rodapé da engine
    lista_itens = dados['Exports'][0]['Table']['Data']
    
    buffer_itens = []
    tamanho_atual = 0
    contador = 1

    for item in lista_itens:
        item_str = json.dumps(item, ensure_ascii=False)
        if (tamanho_atual + len(item_str)) > LIMITE_CARACTERES and buffer_itens:
            # Salva apenas a lista de itens, sem o esqueleto
            salvar(buffer_itens, contador)
            contador += 1
            buffer_itens = []
            tamanho_atual = 0
        
        buffer_itens.append(item)
        tamanho_atual += len(item_str)

    if buffer_itens: salvar(buffer_itens, contador)
    print(f"✅ Geradas {contador} partes focadas apenas em texto!")

def salvar(itens, num):
    nome = os.path.join(pasta_saida, f'parte_{num:03d}.json')
    with open(nome, 'w', encoding='utf-8') as f:
        # Salvamos como uma lista simples [] para a IA não se distrair
        json.dump(itens, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    dividir_json_v2()