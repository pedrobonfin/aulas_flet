import flet as ft


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Image(
            src="images/paisagem.webp"
        ),
        ft.Container(
            content=ft.Text("Paisagem", color=ft.Colors.WHITE, size=32),
            image=ft.DecorationImage(
                src="images/paisagem.webp",
                fit=ft.BoxFit.COVER
            ),
            bgcolor=ft.Colors.BLUE,
            width=300,
            height=600,
            alignment=ft.Alignment(0,0)
        )

    )


ft.run(main)