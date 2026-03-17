"""
Script de Preparação e Filtragem: Conversão de UAsset para JSON.
Objetivo: 
1. Escanear a pasta de arquivos brutos (RAW) em busca de arquivos .uasset.
2. Filtrar apenas os arquivos que contêm strings de texto (usando busca binária rápida).
3. Converter os arquivos filtrados para JSON usando o UAssetGUI via CLI.
"""

import os
import subprocess
import shutil
import traceback
import sys
import mmap
from pathlib import Path
from typing import List

# --- IMPORTANDO CONFIGURAÇÕES ---
# Importa as constantes definidas no config.py
from config import (
    UASSET_GUI_PATH, 
    UE_VERSION,
    PASTA_RAW, 
    PASTA_FILTRADO, 
    PASTA_JSON_ORIGINAL,
    KEYWORDS_BINARIAS
)

# --- DEFINIÇÃO DE CAMINHOS ---
# Usamos 'Path' do pathlib para lidar com caminhos de forma robusta entre diferentes sistemas
PATH_RAW = Path(PASTA_RAW)
PATH_FILTRADO = Path(PASTA_FILTRADO)
PATH_JSON = Path(PASTA_JSON_ORIGINAL)
UASSET_GUI_EXE = Path(UASSET_GUI_PATH)

def validar_pre_requisitos() -> List[str]:
    """
    Verifica se o ambiente está preparado.
    Garante que as pastas de trabalho e o executável externo existam antes de iniciar.
    """
    problemas = []
    
    if not PATH_RAW.exists():
        problemas.append(f"❌ Pasta RAW não encontrada: {PATH_RAW}")
        
    if not UASSET_GUI_EXE.exists():
        problemas.append(f"❌ UAssetGUI não encontrado em: {UASSET_GUI_EXE}")
        
    return problemas

def arquivo_contem_keywords(caminho_arquivo: Path) -> bool:
    """
    Verifica se o arquivo binário contém termos de tradução (ex: 'LocalizedString').
    Usa 'mmap' para mapear o arquivo na RAM, permitindo uma busca extremamente rápida
    sem carregar o arquivo inteiro na memória.
    """
    if caminho_arquivo.stat().st_size == 0:
        return False
    
    try:
        with caminho_arquivo.open('rb') as f:
            # Mapeia o arquivo na memória (acesso de leitura)
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                # Itera sobre todas as keywords permitidas
                for keyword in KEYWORDS_BINARIAS:
                    kw_bytes = keyword if isinstance(keyword, bytes) else keyword.encode('utf-8')
                    # 'find' no mmap é altamente eficiente
                    if mm.find(kw_bytes) != -1:
                        return True
        return False
    except Exception as e:
        print(f"⚠️ Erro ao ler {caminho_arquivo.name}: {e}")
        return False

def passo_1_filtrar() -> bool:
    """
    FILTRAGEM:
    Varre a pasta RAW, identifica quais arquivos UAsset possuem texto (via keywords)
    e copia apenas os necessários para a pasta FILTRADO.
    """
    print(f"\n{'='*60}\n🔍 PASSO 1: FILTRANDO ARQUIVOS UASSET\n{'='*60}")
    
    PATH_FILTRADO.mkdir(parents=True, exist_ok=True)
    PATH_JSON.mkdir(parents=True, exist_ok=True)
    
    arquivos_encontrados = 0
    arquivos_filtrados = 0
    
    print("📁 Buscando arquivos UAsset...")
    
    # Roda recursivamente por todos os arquivos .uasset
    for path_src in PATH_RAW.rglob("*.uasset"):
        arquivos_encontrados += 1
        
        # Filtro binário: só prossegue se houver texto
        if arquivo_contem_keywords(path_src):
            rel_path = path_src.relative_to(PATH_RAW)
            dest = PATH_FILTRADO / rel_path
            
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path_src, dest)
            
            # Copia arquivos auxiliares (.uexp) que acompanham o .uasset
            uexp_src = path_src.with_suffix(".uexp")
            if uexp_src.exists():
                shutil.copy2(uexp_src, dest.with_suffix(".uexp"))
            
            arquivos_filtrados += 1
            print(f"✅ Filtrado: {rel_path}")
            
    print(f"\n📊 RESUMO DO FILTRO:\n   📁 Encontrados: {arquivos_encontrados}\n   ✅ Filtrados: {arquivos_filtrados}")
    return arquivos_filtrados > 0

def converter_uasset_para_json(uasset_path: Path, json_final_path: Path, numero: int, total: int) -> bool:
    """
    CONVERSÃO:
    Chama o UAssetGUI via linha de comando para exportar o binário para JSON.
    """
    rel_path = uasset_path.relative_to(PATH_FILTRADO)
    print(f"[{numero}/{total}] Convertendo: {rel_path}", end=" ", flush=True)
    
    try:
        # Comando: UAssetGUI tojson <origem> <destino> <versao>
        comando = [
            str(UASSET_GUI_EXE),
            "tojson",
            str(uasset_path.absolute()),
            str(json_final_path.absolute()),
            str(UE_VERSION)
        ]
        
        # Cria uma nova janela de processo (esconde o console do CLI)
        creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
        
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            creationflags=creation_flags
        )
        
        # Validação: O JSON foi gerado e não está vazio?
        if json_final_path.exists() and json_final_path.stat().st_size > 100:
            print("✅")
            return True
        else:
            print("❌ Falha na conversão")
            return False
            
    except Exception as e:
        print(f"\n❌ Erro crítico: {e}")
        return False

def passo_2_conversao() -> bool:
    """
    CONVERSÃO EM LOTE:
    Itera sobre os arquivos filtrados e dispara a conversão para cada um.
    """
    print(f"\n{'='*60}\n🔧 PASSO 2: CONVERTENDO UASSET PARA JSON\n{'='*60}")
    
    arquivos_uasset = list(PATH_FILTRADO.rglob("*.uasset"))
    
    if not arquivos_uasset:
        print("❌ Nenhum arquivo encontrado.")
        return False
    
    total = len(arquivos_uasset)
    sucessos = falhas = 0
    
    for i, uasset_path in enumerate(arquivos_uasset, 1):
        rel_path = uasset_path.relative_to(PATH_FILTRADO)
        json_final_path = PATH_JSON / rel_path.with_suffix(".json")
        
        # Pula se já existir (evita processamento duplicado)
        if json_final_path.exists() and json_final_path.stat().st_size > 100:
            print(f"[{i}/{total}] ⏩ Já existe: {rel_path}")
            sucessos += 1
            continue

        json_final_path.parent.mkdir(parents=True, exist_ok=True)
        
        if converter_uasset_para_json(uasset_path, json_final_path, i, total):
            sucessos += 1
        else:
            falhas += 1
            
    print(f"\n📊 RESUMO DA CONVERSÃO:\n   ✅ Sucessos/Existentes: {sucessos}\n   ❌ Falhas: {falhas}")
    return falhas == 0

def main():
    """
    Fluxo Principal: Validação -> Filtragem -> Conversão.
    """
    try:
        print("🚀 INICIANDO WORKFLOW UASSET PARA JSON")
        print(f"{'='*60}")
        
        # 1. Checagem de ambiente
        problemas = validar_pre_requisitos()
        if problemas:
            print("❌ PROBLEMAS ENCONTRADOS:")
            print("\n".join(f"   {p}" for p in problemas))
            return False
        
        # 2. Executa os passos sequencialmente
        if not passo_1_filtrar() or not passo_2_conversao():
            return False
            
        print(f"\n{'='*60}\n🎉 WORKFLOW CONCLUÍDO!\n📁 JSONs prontos em: {PATH_JSON}\n{'='*60}")
        return True
        
    except Exception as e:
        print(f"💥 Erro crítico: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Inicia o script e encerra com código de saída 1 caso falhe
    if not main():
        print("\n🚫 O processo falhou. Verifique os logs.")
        sys.exit(1)