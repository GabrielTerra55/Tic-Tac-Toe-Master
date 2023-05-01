import sys
from controller.controller_tictactoe import ControllerTicTacToe
from view.tela_principal import TelaPrincipal


class ControllerPrincipal:
    def __init__(self):
        self.__controller_tictactoe = ControllerTicTacToe(self)
        self.__tela_principal = TelaPrincipal()

    @property
    def controller_tictactoe(self):
        return self.__controller_tictactoe

    @property
    def tela_principal(self):
        return self.__tela_principal

    def encerra_sistema(self):
        """
        Encerra o sistema

        Returns:
            Não retorna nada
        """
        self.tela_principal.sistema_encerrado()
        sys.exit(1)

    def inicializa_tictactoe(self):
        """
        Inicializa a partida de tictactoe

        Returns:
            Não retorna nada
        """
        self.__controller_tictactoe.disputar()

    def inicializa_sistema(self):
        """
        Inicia o menu de opções para o usuario

        Returns:
            funções definidas pelo usuario
        """
        lista_opcoes = {
            1: self.inicializa_tictactoe,
            0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.tela_principal.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
