import flet as ft
def pagina_de_espera(page: ft.Page) -> ft.View:
    conteudo_da_pagina = [
            ft.Text("Por favor Aguarde")
    ]
    return ft.View('/espera', controls=conteudo_da_pagina, vertical_alignment = ft.MainAxisAlignment.CENTER, horizontal_alignment = ft.CrossAxisAlignment.CENTER)

def pagina_de_votacao(page: ft.Page, controlador: 'Controlador') -> ft.View:
    pauta = controlador.mensagem
    conteudo_da_pagina = [
        
        ft.Container(
            content = ft.Text(
                value=pauta,
                size = 14,
                text_align = ft.TextAlign.CENTER,
                color=ft.colors.BLACK
            ),
            padding=20,
            border=ft.border.all(3, "#39746F"),
            width = 329,
            height = 73

        ),

        ft.Column(
            controls=[

                ft.ElevatedButton(
                    text='A favor',
                    width=117,
                    height=56,
                    bgcolor='#47D147',
                    color=ft.colors.WHITE,
                    on_click=controlador.votar,
                    data=2,
                    style=ft.ButtonStyle(
                        padding = 20,
                        text_style=ft.TextStyle(size=14, weight=ft.FontWeight.NORMAL, font_family='Inter')
                    )
                ),

                ft.ElevatedButton(
                    text='Contra',
                    width=117,
                    height=56,
                    bgcolor='#C83A3A',
                    color=ft.colors.WHITE,
                    on_click=controlador.votar,
                    data=1,
                    style=ft.ButtonStyle(
                        padding = 20,
                        text_style=ft.TextStyle(size=14, weight=ft.FontWeight.NORMAL, font_family='Inter')
                    )
                ),

                ft.ElevatedButton(
                    text='Abster-se',
                    width=117,
                    height=56,
                    bgcolor='#828E82',
                    color=ft.colors.WHITE,
                    on_click=controlador.votar,
                    data=0,
                    style=ft.ButtonStyle(
                        padding = 20,
                        text_style=ft.TextStyle(size=14, weight=ft.FontWeight.NORMAL, font_family='Inter')
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    ]
    return ft.View(
        '/votacao', 
        controls=conteudo_da_pagina, 
        vertical_alignment = ft.MainAxisAlignment.CENTER, 
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        bgcolor = ft.colors.WHITE
        )

def pagina_do_resultado(page: ft.Page, resultado: str) -> ft.View:
    conteudo_da_pagina = [
        ft.Text(value=resultado)
    ]
    return ft.View('/resultado', controls=conteudo_da_pagina, vertical_alignment = ft.MainAxisAlignment.CENTER, horizontal_alignment = ft.CrossAxisAlignment.CENTER)