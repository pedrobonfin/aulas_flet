import flet as ft


def main(page: ft.Page):
    page.bgcolor = "PURPLE"
    def mostrar_mensagem(e):
        page.add(
            ft.Text("Ryōiki Tenkai, Muryōkūsho.")
        )

    page.add(
        ft.Text("Kyoshiki Murasaki"),
        ft.Image(
            src="images/satoru-gojo.jpg",
            width=300,
            height=300
        ),
        ft.Button(
            content="Clique para ativar o poder do mais forte",
            on_click=mostrar_mensagem
        )
    )

ft.run(main)