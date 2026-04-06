import flet as ft

def main(page: ft.Page):
    # Variável com a imagem certa
    imagem_correta = "Sukuna"
    
    # Texto para feedback
    mensagem = ft.Text(
        f"🟣     |     🔴",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.GREEN_200
            e.control.image.opacity = 0.3
            e.control.content.value = "🤩"
            e.control.content.size = 40
            mensagem.value = "Isso aí, o Sukuna ganhou!"
        else:
            e.control.bgcolor = ft.Colors.RED_200
            e.control.image.opacity = 0.3
            e.control.content.value = "😭"
            e.control.content.size = 40
            mensagem.value = f"Não, Satoru Gojo perdeu a luta, tente outra vez."
        
        container_gato.on_click = None
        container_cachorro.on_click = None

        btn_jogar_novamente.visible = True

        page.update()
    
    # Função Jogar Novamente
    def jogar_novamente(e):
        btn_jogar_novamente.visible = False
        mensagem.value = "🟣     |     🔴"

        container_gato.image.opacity = 1.0
        container_gato.on_click = jogar
        container_gato.content.size = 0
        container_gato.content.value = "Satoru Gojo"
        container_gato.bgcolor = ft.Colors.GREY_200

        container_cachorro.image.opacity = 1.0
        container_cachorro.on_click = jogar
        container_cachorro.content.size = 0
        container_cachorro.content.value = "Sukuna"
        container_cachorro.bgcolor = ft.Colors.GREY_200
        
        page.update()

    # Container GATO
    container_gato = ft.Container(
        content=ft.Text(
            "Satoru Gojo",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/gojo.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container CACHORRO
    container_cachorro = ft.Container(
        content=ft.Text(
            "Sukuna",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/sukuna.webp",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.Button(
        "Tentar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Quem venceu a luta entre Satoru Gojo e Sukuna?",
                    size=24,
                    weight="bold"
                ),
                mensagem,
                ft.Row(
                    [
                        container_gato,
                        container_cachorro
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main)