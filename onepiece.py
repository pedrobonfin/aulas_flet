import flet as ft


def main(page: ft.Page):
    def mostrar_mensagem(e):
        page.add(
            ft.Text("Eu vou ser o rei dos piratas.")
        )

    page.add(
        ft.Text("Olá, eu sou o Luffy!"),
        ft.Image(
            src="images/luffy.jpg",
            width=300,
            height=300
        ),
        ft.Button(
            content="Clique Aqui",
            on_click=mostrar_mensagem
        )
    )


ft.run(main)