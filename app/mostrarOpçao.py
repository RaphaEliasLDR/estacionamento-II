import sys
import flet as ft
from datetime import datetime
sys.path.append("app")  # Garante que o Python encontra o módulo

from bancoDados import criar_banco, adicionar_veiculo, excluir_veiculo, listar_veiculos

def main(page: ft.Page):
    page.title = "Cadastro de Veículos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  

    criar_banco()

    cor = ft.TextField(label="Cor", width=200, bgcolor=ft.colors.GREY_200, color=ft.colors.BLACK, border_color=ft.colors.BLACK)
    modelo = ft.TextField(label="Modelo", width=200, bgcolor=ft.colors.GREY_200, color=ft.colors.BLACK, border_color=ft.colors.BLACK)
    placa = ft.TextField(label="Placa", width=200, bgcolor=ft.colors.GREY_200, color=ft.colors.BLACK, border_color=ft.colors.BLACK)
    
    forma_pagamento = ft.Dropdown(
        label="Forma de Pagamento", 
        options=[
            ft.dropdown.Option("Cartão de Crédito"),
            ft.dropdown.Option("Dinheiro"),
            ft.dropdown.Option("Pix")
        ],
        width=200,
        bgcolor=ft.colors.GREY_200,
        color=ft.colors.BLACK,
        border_color=ft.colors.BLACK
    )
    
    data_entrada = ft.TextField(label="Data de Entrada", width=200, bgcolor=ft.colors.GREY_200, color=ft.colors.BLACK, border_color=ft.colors.BLACK)
    
    def calcular_tempo(data_entrada):
        try:
            data_entrada = datetime.strptime(data_entrada, "%Y-%m-%d %H:%M")
            return datetime.now() - data_entrada
        except Exception:
            return None

    def adicionar_novo_veiculo(e):
        if cor.value and modelo.value and placa.value and forma_pagamento.value and data_entrada.value:
            adicionar_veiculo(cor.value, modelo.value, placa.value, forma_pagamento.value, data_entrada.value)
            cor.value, modelo.value, placa.value, forma_pagamento.value, data_entrada.value = "", "", "", None, ""
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()
    
    def editar_veiculo(veiculo):
        """Função para editar um veículo já cadastrado.""" 
        page.dialog = ft.AlertDialog(
            title=ft.Text("Editar Veículo"),
            content=ft.Column([
                ft.TextField(label="Nova Cor", value=veiculo[0]),
                ft.TextField(label="Novo Modelo", value=veiculo[1]),
                ft.TextField(label="Nova Placa", value=veiculo[2]),
            ]),
            actions=[
                ft.TextButton("Salvar", on_click=lambda e: print("Salvar edição")),  # Implementar atualização no banco
                ft.TextButton("Cancelar", on_click=lambda e: page.dialog.close())  # Alteração para fechar o diálogo
            ],
            open=True
        )
        page.update()

    def mostrar_veiculos(e):
        lista_veiculos = listar_veiculos()
        veiculos_exibicao = ft.Column()

        for veiculo in lista_veiculos:
            if len(veiculo) == 4:
                cor_veiculo, modelo_veiculo, placa_veiculo, data_entrada_veiculo = veiculo
                tempo = calcular_tempo(data_entrada_veiculo)
                item_texto = f"\U0001F697 {modelo_veiculo} - {cor_veiculo} - {placa_veiculo} - Tempo: {tempo}"
                
                # Adicionando o veículo dentro de um container estilizado
                veiculos_exibicao.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Text(item_texto, expand=True),
                            ft.IconButton(ft.icons.EDIT, on_click=lambda e, v=veiculo: editar_veiculo(v))
                        ]),
                        bgcolor=ft.colors.GREY_200,
                        padding=10,
                        border_radius=5,
                        border=ft.border.all(1, ft.colors.BLACK),
                        margin=5
                    )
                )

        def voltar(e):
            page.views.pop()  # Remove a tela de veículos ao voltar
            page.go("/")  # Retorna para a tela principal
        
        # Novo container para exibir os veículos cadastrados
        container_veiculos = ft.Container(
            content=ft.Column([
                ft.Text("Veículos Cadastrados", size=20, weight=ft.FontWeight.BOLD),
                veiculos_exibicao,
                ft.ElevatedButton("Voltar", on_click=voltar)
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.colors.WHITE, padding=20, width=500, height=1000,
            border_radius=10, alignment=ft.alignment.center,
            border=ft.border.all(2, ft.colors.BLACK)
        )

        # Contêiner para centralizar o "container_veiculos" e definir a cor de fundo "orange_200"
        page.views.append(ft.View("/veiculos", [
            ft.Container(
                content=container_veiculos,  # Centraliza o conteúdo
                bgcolor=ft.colors.ORANGE_200,  # Cor de fundo "orange_200"
                expand=True,
                alignment=ft.alignment.center  # Centraliza o container dentro da página
            )
        ]))
        page.go("/veiculos")
    
    botao_adicionar = ft.ElevatedButton("Adicionar Veículo", on_click=adicionar_novo_veiculo)
    botao_ver_veiculos = ft.ElevatedButton("Ver Veículos Cadastrados", on_click=mostrar_veiculos)
    
    container_menu = ft.Container(
        content=ft.Column([
            cor, modelo, placa, forma_pagamento, data_entrada, botao_adicionar, botao_ver_veiculos
        ], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor=ft.colors.WHITE, padding=20, width=400, height=800,
        border_radius=10, alignment=ft.alignment.center,
        border=ft.border.all(2, ft.colors.BLACK)
    )
    
    # Adiciona o container menu principal
    page.add(ft.Container(
        content=container_menu,  # Centraliza o conteúdo
        bgcolor=ft.colors.BLUE,  # Cor de fundo do menu
        expand=True,
        alignment=ft.alignment.center  # Centraliza o container dentro da página
    ))

ft.app(target=main)
