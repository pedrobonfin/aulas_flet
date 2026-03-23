import flet as ft
# IMPORTA A BIBLIOTECA FLET E CRIA UM APELIDO(ALIAS)

def main(page: ft.Page):
    page.title = "Meu primeiro App Flet" # Define o título da janela
    page.bgcolor = "blue"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Text("Bem-vindo ao meu app!"),
        ft.Text("Aqui você pode criar o que quiser!!")
    )

ft.run(main)