import flet as ft

def main(page: ft.Page):
    # Configurações da Janela
    page.title = "Gamer Card"
    page.bgcolor = "1E1E1E"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Cabeçalho: Avatar (Emoji) e Nome do Lado
    cabecalho = ft.Row(
        controls=[
            ft.Text("😴", size=60), #Emoji a prova de erros
            ft.Column(
                controls=[
                    ft.Text("bonf4zik4", size=24, weight="bold", color="white"),
                    ft.Text("Nível 999 - :/", size=24, color="grey300"),
                ], spacing=2
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    # Status: Barra de HP, MP e XP
    status_bar = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text("HP: 100", text_align=ft.TextAlign.CENTER, weight="bold"),
                bgcolor="red400", padding=10, border_radius=8, expand=3
            ),
            ft.Container(
                content=ft.Text("MP: 50", text_align=ft.TextAlign.CENTER, weight="bold"),
                bgcolor="blue400", padding=10, border_radius=8, expand=1
            ),
            ft.Container(
                content=ft.Text("XP: 9999", text_align=ft.TextAlign.CENTER, weight="bold"),
                bgcolor="amber400", padding=10, border_radius=8, expand=2
            ),
        ],
        spacing=10
    )

        # BOTÕES: Ações do Jogador
    botoes_acao = ft.Row(
            controls=[
                ft.Button(
                    content="Adicionar Amigo",
                    bgcolor="#36628E",
                    color="white"
                ),
                ft.Button(
                    content="Trocar Itens",
                    bgcolor="red",
                    color="white"
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

        # CARTÃO PRINCIPAL
    cartao = ft.Container(
            content=ft.Column(
                controls=[cabecalho, status_bar, botoes_acao],
                spacing=30
            ),
            bgcolor="#2E2E2E",
            padding=40,
            border_radius=15,
            width=450,
            shadow=ft.BoxShadow(blur_radius=20, color="black") # Aqui vai ser um efeito de som
        )
    page.add(cartao)

ft.run(main)