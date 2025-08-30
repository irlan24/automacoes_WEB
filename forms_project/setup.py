import sys
from cx_Freeze import setup, Executable

# Dependências que devem ser incluídas explicitamente
build_exe_options = {
    "packages": [
        "selenium",
        "customtkinter", 
        "tkinter",
        "threading",
        "time",
        "urllib",
        "urllib.request",
        "urllib.parse",
        "urllib.error",
        "http",
        "http.client",
        "json",
        "base64",
        "subprocess",
        "socket",
        "ssl",
        "collections"
    ],
    "excludes": [
        "test",
        "unittest"
    ],
    "include_files": [
        "senhas.py",
        ("icon.ico", "icon.ico"),
        "constants.py",
        "automation.py",
        "ui.py"
    ]
}

# Configurações específicas para diferentes sistemas operacionais
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Remove a janela do console no Windows

# Configuração do executável
executables = [
    Executable(
        script="main.py",
        base=base,
        target_name="FormsApp.exe",
        icon="icon.ico"
    )
]

# Configuração principal do setup
setup(
    name="FormsApp",
    version="1.0.0",
    description="Aplicação para preenchimento automático de formulários",
    options={"build_exe": build_exe_options},
    executables=executables
)

# Instruções de uso:
# 
# 1. Instale as dependências:
#    pip install cx_freeze selenium customtkinter
#
# 2. Execute o build:
#    python setup.py build
#
# 3. O executável será criado na pasta build/FormsApp/
#
# Para criar um instalador MSI no Windows:
#    python setup.py bdist_msi
#
# Para incluir drivers do Selenium:
# - Descomente as linhas no include_files
# - Baixe chromedriver.exe e/ou msedgedriver.exe
# - Coloque-os na mesma pasta do setup.py
# - Adicione os caminhos corretos no include_files