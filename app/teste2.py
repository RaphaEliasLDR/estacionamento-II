import flet as ft
from bancoDados import criar_banco, adicionar_usuario, validar_login

def main(page: ft.Page):
    page.title = "Sistema de Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    criar_banco()
    
    left_container = ft.Container(
        bgcolor=ft.colors.BLUE,
        width=500,
        height=1000,
        content=ft.Column(
            controls=[ft.Image(src="assets/icone.png", width=500, height=500)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    right_container = ft.Container(
        bgcolor=ft.colors.ORANGE_200,
        width=700,
        height=1000,
    )

    page.add(
        ft.Row(
            controls=[left_container, right_container],
            expand=True,
        )
    )

    texto_login = ft.Text("Login", size=30, weight=ft.FontWeight.BOLD, color="blue")

    right_container.content = ft.Column(
        controls=[texto_login, botao_login(page)],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page.update()

def botao_login(page: ft.Page):
    entrada_nome = ft.TextField(label="Nome", width=500)
    entrada_senha = ft.TextField(label="Senha", password=True, width=500)
    
    botao_entrar = ft.ElevatedButton("Entrar", on_click=lambda e: validar_login_ui(page, entrada_nome, entrada_senha))
    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: mostrar_registro(page))
    
    return ft.Column(
        controls=[
            entrada_nome,
            entrada_senha,
            ft.Row(controls=[botao_entrar, botao_registrar], alignment=ft.MainAxisAlignment.CENTER)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

def mostrar_registro(page: ft.Page):
    page.clean()
    page.add(ft.Text("Tela de Registro", size=30, weight=ft.FontWeight.BOLD, color="blue"))
    
    entrada_nome = ft.TextField(label="Nome de Usuário", width=300)
    entrada_senha = ft.TextField(label="Senha", password=True, width=300)
    
    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: registrar_usuario(page, entrada_nome, entrada_senha))
    botao_voltar = ft.ElevatedButton("Voltar", on_click=lambda e: main(page))
    
    page.add(entrada_nome, entrada_senha, botao_registrar, botao_voltar)
    page.update()

def registrar_usuario(page: ft.Page, entrada_nome: ft.TextField, entrada_senha: ft.TextField):
    adicionar_usuario(entrada_nome.value, entrada_senha.value)
    page.clean()
    page.add(ft.Text("Usuário registrado com sucesso!", color="green"))
    main(page)

def validar_login_ui(page: ft.Page, entrada_nome: ft.TextField, entrada_senha: ft.TextField):
    if validar_login(entrada_nome.value, entrada_senha.value):
        page.clean()
        page.add(ft.Text("Login bem-sucedido!", size=20, color="green"))
    else:
        page.add(ft.Text("Usuário ou senha incorretos.", color="red"))
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
