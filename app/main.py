import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import flet as ft
from app.desenvolvimento import main

if __name__ == "__main__":
    print("Iniciando a aplicação Flet...")
    ft.app(target=main)
