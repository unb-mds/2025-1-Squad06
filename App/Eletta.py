import flet as ft
from servidor import servidor
from servidor import cliente
from views import votante, host


# ----------------- views padrões -----------------
def pagina_inicial(page: ft.Page, controlador: 'Controlador') -> ft.View:
    conteudo_da_pagina = [
        ft.Column(
            [
                ft.ElevatedButton(
                    text="virar votante",
                    width=117,
                    height=56,
                    color=ft.colors.WHITE,
                    bgcolor= "#39746F",
                    on_click=controlador.entrar_na_votacao_como_votante,
                    style=ft.ButtonStyle(
                        padding = 20,
                        text_style=ft.TextStyle(size=13, weight=ft.FontWeight.NORMAL, font_family='Inter')
                    )
                    ),
                ft.ElevatedButton(
                    text="virar host",
                    width=117,
                    height=56,
                    color=ft.colors.WHITE,
                    bgcolor= "#39746F", 
                    on_click=controlador.entrar_na_votacao_como_host,
                    style=ft.ButtonStyle(
                        padding = 20,
                        text_style=ft.TextStyle(size=13, weight=ft.FontWeight.NORMAL, font_family='Inter')
                    )
                    )
            ],
            alignment = ft.MainAxisAlignment.CENTER
        )
    ]
    return ft.View(
        '/', 
        controls=conteudo_da_pagina, 
        vertical_alignment = ft.MainAxisAlignment.CENTER, 
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        bgcolor= ft.colors.WHITE
        )

def pagina_do_resultado(page: ft.Page, resultado: str) -> ft.View:
    conteudo_da_pagina = [
        ft.Text(value=resultado)
    ]
    return ft.View('/resultado', controls=conteudo_da_pagina, vertical_alignment = ft.MainAxisAlignment.CENTER, horizontal_alignment = ft.CrossAxisAlignment.CENTER)

# ---------- logica -------------

class Controlador():
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = 'Elleta'
        self.udp_socket = None
        self.banco_de_dados = None
        self.mensagem = None
        self.process = None
        self.flag_controle = None
        self.page.go('/')

    # ----------- votante -------------
    def entrar_na_votacao_como_votante(self, e) -> None:
        self.udp_socket = cliente.virar_votante()
        self.page.go('/espera')
        pauta = cliente.receber_mensagem(self.udp_socket)
        self.mensagem = pauta
        if self.mensagem != 'votação encerrada':
            self.page.go('/votacao')
        else:
            pass

    def votar(self, e: ft.ControlEvent):
        if e.control.data == 2:
            cliente.votar(self.udp_socket, 'a favor', self.mensagem)
        elif e.control.data == 1:
            cliente.votar(self.udp_socket, 'contra', self.mensagem)
        elif e.control.data == 0:
            cliente.votar(self.udp_socket, 'nulo', self.mensagem)
        self.page.go('/espera')
        self.mensagem = cliente.receber_mensagem(self.udp_socket)
        self.page.go('/resultado')

    # ----------- host -------------
    def entrar_na_votacao_como_host(self, e) -> None:
        self.udp_socket = servidor.virar_host()
        self.banco_de_dados, self.process, self.flag_de_controle = servidor.aguardar_votantes(self.udp_socket)
        self.page.go('/espera_votantes')

    def encerrar_espera_de_votantes(self, e):
        self.flag_de_controle.set()
        self.process.join()
        self.page.go('/criacao_de_pauta')

    def enviar_pauta(self, e: ft.ControlEvent):
        self.process, self.flag_de_controle = servidor.aguardar_votos(self.banco_de_dados, self.udp_socket)
        self.mensagem = e.control.data.value
        self.banco_de_dados.adicionar_pauta(self.mensagem)
        self.banco_de_dados.serializar_dados()
        servidor.mandar_mensagem(self.banco_de_dados, self.udp_socket, self.mensagem)
        self.page.go('/espera_votos')

    def encerrar_espera_de_votos(self, e):
        self.flag_de_controle.set()
        self.process.join()
        self. mensagem = servidor.mostrar_resultados(self.banco_de_dados, self.udp_socket, self.mensagem)
        self.page.go('/resultado')


def main(page: ft.Page) -> None:
    controlador = Controlador(page)
    def mudar_de_pagina(e: ft.ControlEvent) -> None:
        page.views.clear()
        if page.route == '/':
            page.views.append(pagina_inicial(page, controlador))
        
        elif page.route == '/espera':
            page.views.append(votante.pagina_de_espera(page))
        
        elif page.route == '/votacao':
            page.views.append(votante.pagina_de_votacao(page, controlador))

        elif page.route == '/espera_votantes':
            page.views.append(host.pagina_de_espera_votantes(page, controlador))

        elif page.route == '/criacao_de_pauta':
            page.views.append(host.pagina_de_criacao_de_pauta(e.page, controlador))

        elif page.route == '/espera_votos':
            page.views.append(host.pagina_de_espera_votos(page, controlador))

        elif page.route == '/resultado':
            page.views.append(pagina_do_resultado(page, controlador.mensagem))

        page.update()
        
    page.on_route_change = mudar_de_pagina
    page.go('/')
        
ft.app(target=main)
