import flet as ft
from servidor import servidor, cliente

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
