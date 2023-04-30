import os

from model.tictactoe import TicTacToe
from view.tela_tic_tac_toe import TelaTicTacToe


class ControllerTicTacToe:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_tictactoe = TelaTicTacToe()
        self.__tic_tac_toe = TicTacToe()

    @property
    def tela_tictactoe(self):
        return self.__tela_tictactoe

    @property
    def tic_tac_toe(self):
        return self.__tic_tac_toe

    def disputar(self):
        while not self.conferir_fim_da_partida(self.tic_tac_toe.cerquilha, self.tic_tac_toe.jogada):
            jogador = self.definir_jogador()
            self.jogar(jogador)

        # se tiver acabado, deve-se ...

        ganhador = self.tic_tac_toe.ganhador
        if ganhador != 'V':
            self.tela_tictactoe.mostra_ganhador(self.tic_tac_toe.ganhador)
        else:
            self.tela_tictactoe.mostra_empate()

        self.tic_tac_toe.ganhador = None
        self.tic_tac_toe.jogada = 0
        self.tic_tac_toe.jogador = 1
        self.tic_tac_toe.cerquilha = [
            [0 for j in range(3)] for i in range(3)]
        return

    def jogar(self, jogador):
        tabela = self.tic_tac_toe.cerquilha
        self.mostra_tabela(tabela)
        
        while True:
            posicao = self.tela_tictactoe.recolhe_jogada()
            posicao = self.verificar_posicao(posicao, tabela)
            posicao_real = self.converter_em_posicao_real(posicao)
            validade_da_posicao = self.verificar_se_posicao_ja_esta_ocupada(
                posicao_real, tabela)

            if not validade_da_posicao:
                break

        tabela[int(posicao_real[0])][int(posicao_real[1])] = jogador

        self.troca_jogador()
        self.acrescentar_jogada()
        os.system('clear') or None

    def converter_em_posicao_real(self, jogada):
        jogada = int(jogada)

        if jogada <= 3:
            jogada = str(jogada - 1)
            valor = [0, jogada]
            return valor

        elif jogada <= 6:
            valor = str(jogada + 6)
            return valor

        elif jogada <= 9:
            valor = str(jogada + 13)
            return valor

        else:
            raise Exception('Erro de jogada')

    def verificar_posicao(self, posicao, tabela):

        while int(posicao) < 1 or int(posicao) > 9:
            self.tela_tictactoe.opcao_invalida()
            posicao = self.tela_tictactoe.jogada(tabela)

        return posicao

    def verificar_se_posicao_ja_esta_ocupada(self, posicao, tabela):
        return tabela[int(posicao[0])][int(posicao[1])] == 'X' or tabela[int(posicao[0])][int(posicao[1])] == 'O'

    def mostra_tabela(self, tabela):
        self.tela_tictactoe.mostra_tabela(tabela)

    def jogada_maior_que_5(self, jogada):
        return jogada >= 4

    def troca_jogador(self):
        self.tic_tac_toe.jogador += 1

    def acrescentar_jogada(self):
        self.tic_tac_toe.jogada += 1

    def definir_jogador(self):
        if self.tic_tac_toe.jogador % 2 == 1:
            return 'X'
        return 'O'

    def conferir_fim_da_partida(self, tabela, jogada):
        if self.jogada_maior_que_5(jogada):
            # verificação na horizontal

            for i in range(0, 3):
                if tabela[i][0] == tabela[i][1] and tabela[i][1] == tabela[i][2] and type(tabela[i][1]) != int:
                    self.tic_tac_toe.ganhador = tabela[i][0]
                    
                    return True

            # verificação na vertical
            for i in range(0, 3):
                if tabela[0][i] == tabela[1][i] and tabela[1][i] == tabela[2][i] and type(tabela[1][i]) != int:
                    self.tic_tac_toe.ganhador = tabela[1][i]
                    
                    return True

            if tabela[0][0] == tabela[1][1] and tabela[1][1] == tabela[2][2] and type(tabela[1][1]) != int:
                self.tic_tac_toe.ganhador = tabela[1][1]
                
                return True

            if tabela[0][2] == tabela[1][1] and tabela[1][1] == tabela[2][0] and type(tabela[1][1]) != int:
                self.tic_tac_toe.ganhador = tabela[1][1]
                
                return True

        if jogada == 8:
            self.tic_tac_toe.ganhador = 'V'
            return True

        return
