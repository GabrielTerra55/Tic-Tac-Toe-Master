import os

from game.model.tictactoe import TicTacToe
from game.view.tela_tic_tac_toe import TelaTicTacToe


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
        """
        Método principal que controla a partida, se a ganhador ou houve empate.

        Returns:
            Não retorna nada.
        """
        while not self.conferir_fim_da_partida(self.tic_tac_toe.cerquilha, self.tic_tac_toe.jogada):
            jogador = self.definir_jogador()
            self.jogar(jogador)


        ganhador = self.tic_tac_toe.ganhador
        if ganhador != 'V':
            self.tela_tictactoe.mostra_ganhador(self.tic_tac_toe.ganhador)
        else:
            self.tela_tictactoe.mostra_empate()

        self.mostra_tabela()
        self.reseta_tic_tac_toe()
        return

    def jogar(self, jogador):
        """
        Executa uma rodada do jogo, validando as posições passadas e as salvando na matriz 'cerquilha'.

        Returns:
            Não retorna nada
        """
        self.mostra_tabela()
        tabela = self.tic_tac_toe.cerquilha
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
        """
        Converte a posição relativa passada pelo usuario para uma posição absoluta referente a matriz 'cerquilha'.

        Args:
            str: valor da posição relativa
        
        Returns:
            str: a posição absoluta da matriz 'cerquilha'.

        Exemplo:
            >> 6
            '12'        1 referente a linha e 2 referente a coluna 
            >> 9
            '22'        2 referente a linha e 2 referente a coluna 
        """
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
        """
        Verifica se a posição relativa passada pelo usuario existe na matriz 'cerquilha'. 
        Se não existe ele a solicita novamente e a confere. Repete o processo até que
        a posição seja valida.

        Args:
            str: valor da possivel posição relativa.
        
        Returns:
            str: a posição relativa da matriz 'cerquilha' validada.

        Exemplo:
            >> 30
            '5'        solicitou a entrada novamente ate ser validada
            >> 9
            '9'        não foi necessário ser validada
        """
        while int(posicao) < 1 or int(posicao) > 9:
            self.tela_tictactoe.opcao_invalida()
            posicao = self.tela_tictactoe.jogada(tabela)

        return posicao

    def verificar_se_posicao_ja_esta_ocupada(self, posicao, tabela):
        """
        Verifica se a posição absoluta da matriz 'cerquilha' passada está ocupada.

        Args:
            str: valor da possivel posição absoluta.
        
        Returns:
            bool: True ou False

        Exemplo:
            >> 11
            'False'        posição não ocupada
            >> 02
            'True'        posição ocupada
        """
        return tabela[int(posicao[0])][int(posicao[1])] == 'X' or tabela[int(posicao[0])][int(posicao[1])] == 'O'

    def mostra_tabela(self):
        """
        Exibe a tela com a matriz 'cerquilha' com os devidos valores preenchidos ou não.

        Returns:
        Não retorna nada.

        Exemplo:
            >> 30
            '5'        solicitou a entrada novamente ate ser validada
            >> 9
            '9'        não foi necessário ser validada
        """
        self.tela_tictactoe.mostra_tabela(self.tic_tac_toe.cerquilha)

    def reseta_tic_tac_toe(self):
        """
        Reseta os valore da classe TicTacToe. 'jogadas', 'ganhador', 'jogada' e a matriz 'cerquilha'
        
        Returns:
            Não retorna nada
        """
        self.tic_tac_toe.ganhador = None
        self.tic_tac_toe.jogada = 0
        self.tic_tac_toe.jogador = 1
        self.tic_tac_toe.cerquilha = [
            [0 for j in range(3)] for i in range(3)]

    def jogada_maior_que_5(self, jogada):
        """
        Verifica se foi feito 5 jogadas ou mais na partida.

        Args:
            int: numero de jogadas feitas. Essas jogadas se encontram entre os atributos
            da classe TicTacToe
        
        Returns:
            bool: True ou False

        Exemplo:
            >> 4
            False        Não foi feito 5 jogadas ou mais
            >> 6
            True         Foi feito 5 jogadas ou mais
        """
        return jogada >= 4

    def troca_jogador(self):
        """
        Alterna o jogador para a proxima rodada direto no atributo da classe acrescentado + 1 em um contador. 

        Returns:
            Não retorna nada
        """
        self.tic_tac_toe.jogador += 1

    def acrescentar_jogada(self):
        """
        Acrescenta no contador de jogadas + 1. Altera no direto no atributo da classe
        
        Returns:
            Não retorna nada
        """
        
        self.tic_tac_toe.jogada += 1

    def definir_jogador(self):
        """
        Define quem é o jogador que ira jogar na rodada. X ou O
        
        Returns:
            Retorna o Jogador
        Exemplo:
            >> 2
            'O'
            >> 5
            'X'
        """
        if self.tic_tac_toe.jogador % 2 == 1:
            return 'X'
        return 'O'

    def conferir_fim_da_partida(self, tabela, jogada):
        """
        Define o fim da partida conferindo: se existe algum vencedor ou se deu velha .

        Args:
            list: Tabela do jogo 'cerquilha'
            int:  Numero de jogadas
        
        Returns:
            bool: True ou False
        """
        if self.jogada_maior_que_5(jogada):

            for i in range(0, 3):
                if tabela[i][0] == tabela[i][1] and tabela[i][1] == tabela[i][2] and type(tabela[i][1]) != int:
                    self.tic_tac_toe.ganhador = tabela[i][0]
                    
                    return True

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

        if jogada == 9:
            self.tic_tac_toe.ganhador = 'V'
            return True

        return False
