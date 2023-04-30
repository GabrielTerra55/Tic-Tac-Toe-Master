from model.tictactoe import TicTacToe
from view.tela_principal import *


class ControllerTicTacToe:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_tictactoe = None
        self.__tic_tac_toe = TicTacToe()

    def disputar(self):
        while not self.conferir_fim_da_partida(self.__tic_tac_toe.cerquilha, self.__tic_tac_toe.jogada):
            jogador = self.definir_jogador()
            self.jogar(jogador)
        
        # se tiver acabado, deve-se ...
        
        ganhador = self.__tic_tac_toe.ganhador
        if ganhador != 'V':
            self.__tela_tictactoe.mostra_ganhador(self.__tic_tac_toe.ganhador)
        else:
            self.__tela_tictactoe.mostra_empate(self.__tic_tac_toe.ganhador)
        return




# ================================== J O G A D A =========================================
    def jogar(self, jogador):
        tabela = self.__tic_tac_toe.cerquilha
        self.__tela_tictactoe.mostra_tabela(tabela)
        posicao = self.__tela_tictactoe.recolhe_jogada()
        
        while True:
            posicao = self.verificar_posicao(posicao, tabela)
            posicao_real = self.converter_em_posicao_real(posicao)
            validade_da_posicao = self.verificar_se_posicao_ja_esta_ocupada(
                posicao_real, tabela)
            
            if not validade_da_posicao:
                break

        tabela[int(posicao_real[0])][int(posicao_real[1])] = jogador

        self.troca_jogador()
        self.acrescentar_jogada()
        

    def converter_em_posicao_real(self, jogada):
        jogada = int(jogada)

        if jogada <= 3:
            jogada = str(jogada - 1)
            valor = [0, jogada]
            return valor

        elif jogada <= 6:
            valor = str(jogada - 6)
            return valor

        elif jogada <= 9:
            valor = str(jogada - 13)
            return valor

        else:
            raise Exception('Erro de jogada')

    def verificar_posicao(self, posicao, tabela):

        while posicao < 1 or posicao > 9:
            self.__tela_tictactoe.opcao_invalida()
            posicao = self.__tela_tictactoe.jogada(tabela)

        return posicao

    def verificar_se_posicao_ja_esta_ocupada(self, posicao, tabela):        
        return tabela[int(posicao[0])][int(posicao[1])] == 'X' or tabela[posicao[0]][posicao[1]] == 'O'
# =======================================================================================================

    def jogada_maior_que_5(self, jogada):
        return jogada >= 5

    def troca_jogador(self):
        self.__tic_tac_toe.jogador += 1
    
    def acrescentar_jogada(self):
        self.__tic_tac_toe.jogada += 1
    
    def definir_jogador(self):
        if self.__tic_tac_toe.jogador % 2 == 1:
            return 'X'
        return 'O'

    def conferir_fim_da_partida(self, tabela, jogada):
        if self.jogada_maior_que_5(jogada):
            # verificação na horizontal
            
            for i in range(0, 3):
                if tabela[i][0] == tabela[i][1] and tabela[i][1] == tabela[i][2]:
                    self.__tic_tac_toe.__ganhador = tabela[i][1]
                    return True
            
            #verificação na vertical
            for i in range(0, 3):
                if tabela[0][i] == tabela[1][i] and tabela[1][i] == tabela[2][i]:
                    self.__tic_tac_toe.__ganhador = tabela[1][i]
                    return True

            if tabela[0][0] == tabela[1][1] and tabela[1][1] == tabela[2][2]:
                self.__tic_tac_toe.__ganhador = tabela[1][1]
                return True
            
            if tabela[2][0] == tabela[1][1] and tabela[1][1] == tabela[0][2]:
                self.__tic_tac_toe.__ganhador = tabela[1][1]
                return True
            
        if jogada == 9:
            self.__tic_tac_toe.__ganhador = 'V'
            return True

        return 