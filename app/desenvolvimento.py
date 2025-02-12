import flet as ft
from app.bancoDados import criar_banco, adicionar_usuario, validar_login


def main(page: ft.Page):
    criar_banco()

    # Container azul que ocupa toda a tela
    background_container = ft.Container(
        bgcolor=ft.colors.BLUE,
        width=page.width,
        height=page.height,
        content=ft.Column(
            controls=[login_form(page)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(background_container)

    page.update()

def login_form(page: ft.Page):
    texto_login = ft.Text(
        value="Login", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="blue"
        )
    )

    return ft.Container(
        content=ft.Column(
            controls=[texto_login, botao_login(page)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,  # Fundo branco para o container de login
        border_radius=15,
        width=400,
        height=400,
        alignment=ft.alignment.center,
        border=ft.border.all(2, ft.colors.BLACK)  # Borda preta adicionada
    )

def botao_login(page: ft.Page):
    entrada_nome = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.PERSON, size=20, color="blue"),
            ft.TextField(label="Nome", bgcolor="white", width=300)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    senha_icon = ft.Icon(name=ft.icons.LOCK, size=20, color="blue")
    entrada_senha = ft.Row(
        controls=[
            senha_icon,
            ft.TextField(label="Senha", password=True, bgcolor="white", width=300)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    botao_entrar = ft.ElevatedButton("Entrar", on_click=lambda e: validar_login_ui(page, entrada_nome, entrada_senha))
    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: mostrar_registro(page))

    return ft.Column(
        controls=[
            entrada_nome,
            entrada_senha,
            ft.Row(
                controls=[botao_entrar, botao_registrar],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

def validar_login_ui(page: ft.Page, entrada_nome: ft.Row, entrada_senha: ft.Row):
    nome = entrada_nome.controls[1].value
    senha = entrada_senha.controls[1].value

    if validar_login(nome, senha):
        page.clean()
    else:
        page.add(ft.Text("Usuário ou senha incorretos.", color="red"))
    
    page.update()

def mostrar_registro(page: ft.Page):
    page.clean()

    textoDeRegistro = ft.Text(
        value="Tela de Registro", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="blue"
        )
    )

    entrada_nome = ft.Row(
        controls=[ft.Icon(name=ft.icons.PERSON, size=20, color="blue"),
                  ft.TextField(label="Nome de Usuário", bgcolor="white", width=300)],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    entrada_senha = ft.Row(
        controls=[ft.Icon(name=ft.icons.LOCK, size=20, color="blue"),
                  ft.TextField(label="Senha", password=True, bgcolor="white", width=300)],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: registrar_usuario(page, entrada_nome, entrada_senha))
    botao_voltar = ft.ElevatedButton("Voltar", on_click=lambda e: main(page))

    container_formulario = ft.Container(
        content=ft.Column(
            controls=[textoDeRegistro, entrada_nome, entrada_senha, botao_registrar, botao_voltar],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        width=400,
        height=400,
        alignment=ft.alignment.center,
        border=ft.border.all(2, ft.colors.BLACK)  # Borda preta adicionada
    )

    page.add(
        ft.Container(
            content=container_formulario,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor=ft.colors.ORANGE_200
        )
    )

    page.update()

def registrar_usuario(page: ft.Page, entrada_nome: ft.Row, entrada_senha: ft.Row):
    nome = entrada_nome.controls[1].value
    senha = entrada_senha.controls[1].value

    adicionar_usuario(nome, senha)
    page.add(ft.Text("Usuário registrado com sucesso!", color="green"))

    page.clean()
    main(page)
