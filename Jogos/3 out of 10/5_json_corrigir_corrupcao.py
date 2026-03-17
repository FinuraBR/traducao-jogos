"""
Script de Finalização: Conversão JSON para UAsset.
Objetivo: Converter os arquivos JSON já traduzidos de volta para o formato de 
binary de Unreal Engine (.uasset) utilizando a CLI do UAssetGUI, 
realizar backups de segurança e limpar os arquivos temporários do sistema.
"""

import json
import os
import subprocess
import shutil
import time
import traceback
import sys

# --- IMPORTANDO CONFIGURAÇÕES DO CONFIG.PY ---
from config import (
    UASSET_GUI_PATH, UE_VERSION,
    PASTA_RAW, PASTA_FILTRADO, PASTA_JSON_ORIGINAL, 
    PASTA_MOD_FINAL, ARQUIVO_STATUS, ARQUIVO_JSON_TRADUZIDO,
    BASE_DIR, PASTA_PARTES_1, PASTA_PARTES_2, PASTA_PARTES_3
)

def verificar_pre_requisitos(status) -> bool:
    """
    Realiza uma verificação de sanidade antes de começar.
    Garante que todos os arquivos necessários (JSON original, traduzido e o executável CLI)
    existem e estão acessíveis.
    """
    problemas = []
    
    # Valida se o arquivo de controle de fluxo existe
    if not os.path.exists(ARQUIVO_STATUS):
        problemas.append("❌ Arquivo de status (projeto_status.json) não encontrado.")
    
    # Valida se a tradução final foi gerada
    if not os.path.exists(ARQUIVO_JSON_TRADUZIDO):
        problemas.append("❌ Arquivo JSON traduzido (json_PTBR.json) não encontrado. Execute o Passo 4 primeiro.")
    
    # Valida se o UAssetGUI (ferramenta externa) está no caminho configurado
    if not os.path.exists(UASSET_GUI_PATH):
        problemas.append(f"❌ UAssetGUI (CLI) não encontrado em: {UASSET_GUI_PATH}")
    
    # Valida o caminho do JSON original (usado como referência)
    orig_json_src = os.path.join(PASTA_JSON_ORIGINAL, status['subpath'], f'{status["nome"]}.json')
    if not os.path.exists(orig_json_src):
        problemas.append(f"❌ Arquivo JSON original não encontrado: {orig_json_src}")
    
    if problemas:
        print("\n❌ PROBLEMAS CRÍTICOS ENCONTRADOS:")
        for p in problemas: print(f"   {p}")
        return False
    return True

def executar_backup_seguro(status) -> bool:
    """
    Cria uma cópia de segurança dos arquivos .uasset e .uexp originais
    adicionando a extensão .bak antes de sobrescrevê-los.
    """
    try:
        nome = status['nome']
        subpath = status['subpath']
        
        # Localiza o UAsset que será substituído
        original_uasset_src = os.path.join(PASTA_FILTRADO, subpath, f'{nome}.uasset')
        original_uexp_src = original_uasset_src.replace(".uasset", ".uexp")
        
        print("💾 Executando backup do UAsset original antes de sobrescrever...")
        
        # Backup do arquivo principal
        backup_uasset_path = original_uasset_src + ".bak"
        if os.path.exists(original_uasset_src):
            shutil.copy2(original_uasset_src, backup_uasset_path)
            print(f"✅ Backup UAsset criado: {backup_uasset_path}")
        else:
            print(f"⚠️ UAsset original não encontrado em '{original_uasset_src}' para backup.")
        
        # Backup do arquivo de dados associado (uexp), comum em Unreal Engine 4.25+
        backup_uexp_path = original_uexp_src + ".bak"
        if os.path.exists(original_uexp_src):
            shutil.copy2(original_uexp_src, backup_uexp_path)
            print(f"✅ Backup UEXP criado: {backup_uexp_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro durante backup: {e}")
        return False

def limpar_arquivos_temporarios(status) -> bool:
    """
    Remove todos os arquivos e pastas temporárias criadas durante o fluxo de tradução,
    deixando o ambiente limpo para um próximo arquivo.
    """
    try:
        print("🧹 Limpando arquivos temporários e intermediários...")
        
        # Arquivos globais de controle
        arquivos_para_remover = [ARQUIVO_JSON_TRADUZIDO, ARQUIVO_STATUS]
        
        # Pastas de processamento
        pastas_para_limpar = [PASTA_PARTES_1, PASTA_PARTES_2, PASTA_PARTES_3]
        
        # Esvazia as pastas de trabalho
        for pasta in pastas_para_limpar:
            if os.path.exists(pasta):
                for arquivo in os.listdir(pasta):
                    caminho_arquivo = os.path.join(pasta, arquivo)
                    try:
                        if os.path.isfile(caminho_arquivo):
                            os.remove(caminho_arquivo)
                    except Exception: 
                        pass # Silencia erros caso o arquivo esteja bloqueado
        
        # Remove arquivos de controle
        for arquivo in arquivos_para_remover:
            if os.path.exists(arquivo):
                try:
                    os.remove(arquivo)
                    print(f"✅ Removido: {os.path.basename(arquivo)}")
                except Exception: 
                    pass
        
        print("✅ Limpeza completa concluída!")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante limpeza: {e}")
        return False

def executar_conversao_json_para_uasset_cli(status) -> bool:
    """
    Invoca o UAssetGUI via linha de comando para transformar o JSON traduzido
    de volta no formato binário da Unreal Engine.
    """
    nome = status['nome']
    subpath = status['subpath']
    
    # Define o arquivo de entrada (JSON final) e o de saída (UAsset)
    input_json_path = os.path.abspath(ARQUIVO_JSON_TRADUZIDO)
    dest_folder = os.path.join(PASTA_MOD_FINAL, subpath)
    os.makedirs(dest_folder, exist_ok=True) 
    output_uasset_path = os.path.abspath(os.path.join(dest_folder, f'{nome}.uasset'))
    
    print(f"🤖 Convertendo JSON traduzido para UAsset via CLI: {nome}.json")
    print(f"📍 UAsset de saída: {output_uasset_path}")
    
    try:
        # Monta o comando CLI: UAssetGUI fromjson [origem] [destino] [versao_ue]
        comando = [
            str(UASSET_GUI_PATH), 
            "fromjson", 
            str(input_json_path), 
            str(output_uasset_path), 
            str(UE_VERSION)
        ]
        
        # Configuração para não abrir uma janela do console (execução silenciosa)
        creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
        
        # Executa e aguarda o término
        resultado = subprocess.run(
            comando, 
            capture_output=True, 
            text=True, 
            check=False, 
            creationflags=creation_flags
        )

        # Validação do sucesso da operação baseada no código de retorno e existência do arquivo
        if resultado.returncode == 0:
            if os.path.exists(output_uasset_path) and os.path.getsize(output_uasset_path) > 100:
                print("✅ Arquivo UAsset criado com sucesso!")
                return True
            else:
                print("❌ Conversão via CLI falhou: arquivo de saída não gerado ou vazio.")
                print(f"Saída: {resultado.stdout}")
                return False
        else:
            print(f"❌ UAssetGUI CLI retornou erro {resultado.returncode}.")
            print(f"Erros: {resultado.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao executar UAssetGUI CLI: {e}")
        traceback.print_exc()
        return False

def main() -> bool:
    """
    Fluxo principal: Carrega status -> Verifica -> Converte -> Backup -> Limpa.
    """
    try:
        print(f"\n{'='*60}")
        print(f"🛠️ INICIANDO CONVERSÃO FINAL (JSON -> UASSET) VIA CLI")
        print(f"{'='*60}")
        
        # Carrega o estado atual (qual arquivo estamos processando)
        if not os.path.exists(ARQUIVO_STATUS):
            print("❌ Arquivo de status (projeto_status.json) não encontrado. Rode o Gerente.")
            return False
        
        with open(ARQUIVO_STATUS, 'r', encoding='utf-8') as f:
            status = json.load(f)
        
        print(f"📦 Processando: {status['nome']}")
        
        # 1. Checagem inicial
        if not verificar_pre_requisitos(status): 
            return False
        
        # 2. Conversão propriamente dita
        sucesso_conversao = executar_conversao_json_para_uasset_cli(status)
        
        # 3. Pós-processamento apenas se a conversão funcionou
        if sucesso_conversao:
            executar_backup_seguro(status)
            limpar_arquivos_temporarios(status)
            
            print(f"\n🎉 CONVERSÃO FINALIZADA COM SUCESSO!")
            print(f"📁 UAsset salvo em: {PASTA_MOD_FINAL}")
            time.sleep(0.1)
            return True
        else:
            print(f"\n❌ Falha na conversão do arquivo {status['nome']} para UAsset.")
            time.sleep(0.1)
            return False
            
    except Exception as e:
        print(f"💥 Erro crítico no script: {e}")
        traceback.print_exc()
        time.sleep(0.1)
        return False

if __name__ == "__main__":
    # Execução e controle de código de saída (1 para erro, nada/0 para sucesso)
    resultado_sucesso = main()
    
    if not resultado_sucesso:
        print("\n🚫 O PROCESSO FINAL FALHOU. Verifique os logs acima.")
        sys.exit(1)
    else:
        print("\n✨ Processo final concluído com sucesso!")