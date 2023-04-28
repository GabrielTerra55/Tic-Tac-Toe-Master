from model.tictactoe import TicTacToe
from view.tela_principal import *


class ControllerTicTacToe:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_tictactoe = None
        self.__tic_tac_toe = TicTacToe()

    def jogada(self):
        tabela = self.__tic_tac_toe.cerquilha
        posicao = self.__tela_tictactoe.jogada(tabela)
