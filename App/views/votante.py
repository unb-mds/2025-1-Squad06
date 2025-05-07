import flet as ft
def pagina_de_espera(page: ft.Page) -> ft.View:
    conteudo_da_pagina = [
            ft.Text("Por favor Aguarde")
    ]
    return ft.View('/espera', controls=conteudo_da_pagina, vertical_alignment = ft.MainAxisAlignment.CENTER, horizontal_alignment = ft.CrossAxisAlignment.CENTER)

def pagina_de_votacao(page: ft.Page, controlador: 'Controlador') -> ft.View:
    pauta = controlador.mensagem
    conteudo_da_pagina = [
        ft.Column(
            [
                ft.Text(value=pauta),
                ft.ElevatedButton('A favor', on_click=controlador.votar, data=2),
                ft.ElevatedButton('Contra', on_click=controlador.votar, data=1),
                ft.ElevatedButton('Abster-se', on_click=controlador.votar, data=0)
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
    ]
    return ft.View('/votacao', controls=conteudo_da_pagina, vertical_alignment = ft.MainAxisAlignment.CENTER, horizontal_alignment = ft.CrossAxisAlignment.CENTER)

def pagina_do_resultado(page: ft.Page, resultado: str) -> ft.View:
    conteudo_da_pagina = [
        ft.Text(value=resultado)
    ]
    return ft.View('/resultado', controls=conteudo_da_pagina, vertical_alignment = ft.MainAxisAlignment.CENTER, horizontal_alignment = ft.CrossAxisAlignment.CENTER)
