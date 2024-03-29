import sys
from cx_Freeze import setup, Executable




# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
icon = "icon.ico"


if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Gerador de Relatorio",
        version = "1.0",
        description = "Aplicativo para Gerar Relatorio Pre-Evento",
        options = {"build_exe": build_exe_options},
        executables = [Executable("tela_principal.py", base=base,icon=icon)]
        )
