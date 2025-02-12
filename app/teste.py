import flet as ft

def main(page: ft.Page):
    page.title = "Meu App no Navegador"
    page.add(ft.Text("Olá, Flet na Web!"))

# Executa no navegador
ft.app(target=main, view=ft.WEB_BROWSER)
