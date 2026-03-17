"""
Arquivo de Configuração Global.
Este script centraliza todos os parâmetros, caminhos de pastas, regras de filtro
e credenciais. Alterações aqui impactam todo o pipeline de tradução.
"""

import os
import re
from typing import List

# === CONFIGURAÇÃO BÁSICA ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Pastas de entrada bruta (arquivos extraídos do jogo) e filtrada (arquivos prontos para JSON)
PASTA_RAW = r"D:\EP1\1_RAW"
PASTA_FILTRADO = r"D:\EP1\2_FILTRADO"

# ==============================================================================
#                      CONFIGURAÇÃO DE REGRAS ESTRITAS (Filtros de Extração)
# ==============================================================================

# Regex para filtrar "lixo" que não precisa de tradução (números, IDs, URLs, códigos)
REGEX = re.compile(
    r'^[\d\s\W_]+$|'             # Apenas números, espaços e símbolos (ex: "10/10", ":", "100")
    r'^[a-zA-Z]$|'                # Apenas uma letra única (ex: "L", "R", "X")
    r'^www\..*|^https?://.*|'     # URLs
    r'^#\d+$'                     # IDs de cor ou número (ex: #15)
)

# 1. OBRIGATÓRIO: Define quais tipos de 'History' são válidos para tradução
REQUIRED_HISTORY_TYPE = { "Base", "None", "NamedFormat" }

# 2. PROIBIDO: Se o objeto tiver esta flag, ele é considerado "imutável" (não pode ser traduzido)
FORBIDDEN_FLAG = "Immutable"

# 3. WHITELIST: Define quais tipos de objetos JSON podem conter texto traduzível
WHITELIST_TYPES = {
    "TextProperty", 
    "TextPropertyData", 
    "FStringTable", 
    "StringTableExport",
    "StrProperty"
}

# 4. BLACKLIST TÉCNICA: Palavras que a IA pode confundir, mas que não devem ser traduzidas
BLACKLIST_CONTEUDO = {
    "cutscene"
}

# 5. NOMES DE PROPRIEDADE: Variáveis de sistema que não devem sofrer alteração
BLACKLIST_NOMES_VARIAVEL = {
    "internalname", "classname", "tagname"
}

# --- CONFIGURAÇÕES DE REENVIO (Resiliência) ---
TIMEOUT_LIMITE = 180  # Tempo máximo (segundos) que o script aguarda a resposta da IA
MAX_TENTATIVAS = 3    # Tentativas de reenvio caso a IA falhe por instabilidade

# === CONFIGURAÇÃO DE FERRAMENTAS EXTERNAS (Unreal Engine) ===
# Caminho para o executável do UAssetGUI (usado para converter JSON <-> UAsset)
UASSET_GUI_PATH = r"D:\Ferramentas\UAssetGUI.exe"
UE_VERSION = "VER_UE4_25"    # Versão usada no processo fromjson

# Define o tamanho máximo de caracteres por arquivo de parte (evita erro de contexto da IA)
LIMITE_CARACTERES_POR_PARTE = 8000

# --- CONFIGURAÇÃO PUTER / IA ---
USA_EXTERNO = True           # Se True, usa API Cloud (Puter). Se False, usa Ollama (Local).
API_KEY = ""                 # Chave de API da sua conta Puter
# Seleção de modelo para a API Cloud
MODELO_EXTERNO = ["qwen/qwen3.5-122b-a10b"] 

# === CONFIGURAÇÃO DA IA (Local) ===
MODELO_IA = "deepseek-v3.1:671b-cloud"
TEMP_TRADUCAO = 0.6          # Criatividade da tradução
TEMP_VERIFICACAO = 0.3       # Rigidez da verificação (mais baixo é melhor)

# === ESTRUTURA DE PASTAS (Fluxo de trabalho) ===
PASTA_JSON_ORIGINAL = os.path.join(BASE_DIR, "3_JSON_ORIGINAL") # Onde os JSONs extraídos ficam
PASTA_MOD_FINAL = os.path.join(BASE_DIR, "Traducao_PTBR_P")     # Onde os UAssets prontos são salvos

# Pastas de processamento intermediário (Pipeline)
PASTA_PARTES_1 = os.path.join(BASE_DIR, "4_partes_para_traduzir")      # JSON dividido em pedaços
PASTA_PARTES_2 = os.path.join(BASE_DIR, "5_partes_traduzidas")         # Retorno da IA
PASTA_PARTES_3 = os.path.join(BASE_DIR, "6_partes_verificadas")       # Validado e pronto para injetar

# === ARQUIVOS DE CONTROLE ===
ARQUIVO_JSON_TRADUZIDO = os.path.join(BASE_DIR, "json_PTBR.json")      # Arquivo final de injeção
ARQUIVO_STATUS = os.path.join(BASE_DIR, "projeto_status.json")        # Guarda o progresso do loop

# === KEYWORDS PARA FILTRO BINÁRIO (Passo 0) ===
# Estas keywords são usadas para escanear arquivos .uasset rapidamente antes de converter.
# Servem para descartar arquivos que não possuem texto.
KEYWORDS_BINARIAS: List[bytes] = {
    # Versões em UTF-8 (texto puro)
    b"LocalizedString",
    b"CultureInvariantString",
    b"TextPropertyData", 
    b"TextProperty",
    b"SourceString",
    b"FStringTable",
    b"StringTableExport",
    b"StrProperty",
    b"DisplayString",

    # Versões em UTF-16 (como a Unreal Engine salva internamente nos binários)
    b'L\x00o\x00c\x00a\x00l\x00i\x00z\x00e\x00d\x00S\x00t\x00r\x00i\x00n\x00g\x00',
    b'C\x00u\x00l\x00t\x00u\x00r\x00e\x00I\x00n\x00v\x00a\x00r\x00i\x00a\x00n\x00t\x00S\x00t\x00r\x00i\x00n\x00g\x00',
    b'T\x00e\x00x\x00t\x00P\x00r\x00o\x00p\x00e\x00r\x00t\x00y\x00D\x00a\x00t\x00a\x00',
    b'T\x00e\x00x\x00t\x00P\x00r\x00o\x00p\x00e\x00r\x00t\x00y\x00',
    b'S\x00o\x00u\x00r\x00c\x00e\x00S\x00t\x00r\x00i\x00n\x00g\x00',
    b'F\x00S\x00t\x00r\x00i\x00n\x00g\x00T\x00a\x00b\x00l\x00e\x00',
    b'S\x00t\x00r\x00i\x00n\x00g\x00T\x00a\x00b\x00l\x00e\x00E\x00x\x00p\x00o\x00r\x00t\x00',
    b'S\x00t\x00r\x00P\x00r\x00o\x00p\x00e\x00r\x00t\x00y\x00',
    b'D\x00i\x00s\x00p\x00l\x00a\x00y\x00S\x00t\x00r\x00i\x00n\x00g\x00',
}

# Chaves reais no JSON que possuem texto traduzível para o script de injeção
CHAVES_DE_TEXTO = {
    "SourceString",
    "LocalizedString",
    "CultureInvariantString",
    "DisplayString"
}