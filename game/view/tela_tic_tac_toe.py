class TelaTicTacToe:
    def jogada(self, tabela):
        """
        Exibe a matriz 'cerquilha' e recolhe a jogada do usuario

        Args:
            list: Tabela do jogo 'cerquilha'

        Returns:
            str: retorna a posição relativa do jogador fornecida
        """
        self.mostra_tabela(tabela)
        posiçõa_de_jogada = self.recolhe_jogada()
        return posiçõa_de_jogada

    def opcao_invalida(self):
        """
        Exibe uma mensagem informando que a entrada fornecida esta invalida

        Returns:
            Não retorna nada
        """
        print(20 * '*')
        print('POR FAVOR DIGITE UMA VALOR VÁLIDA!')
        print(20 * '*')

    def mostra_tabela(self, tabela):
        """
        Exibe a matriz 'cerquilha' com os dados devidamente formatados

        Returns:
            Não retorna nada
        """
        mostrador = 1
        for i in range(0, 3):
            for c in range(0, 3):
                if tabela[i][c]:
                    print(f'[{tabela [i][c]:^3}]', end=' ')
                else:
                    print(f'[{mostrador:^3}]', end=' ')
                mostrador += 1
            print()

    def recolhe_jogada(self):
        """
        Exibe uma mensagem solicitando ao usuario que insira a jogada

        Returns:
            str: a posição relativa da jogada
        
        Exemplo:
            >> 6
            6
        """
        print(20 * '-=')
        jogada = input(' INSIRA A POSIÇÃO DA JOGADA: ')
        print(20 * '-=')
        return jogada

    def mostra_ganhador(self, resultado):
        """
        Exibe uma mensagem informando o ganhador da partida

        Args:
            str: Parametro do ganhador

        Returns:
            Não retorna nada
        
        Exemplo:
            >> X
            X F O I  O  V E N C E D O R  D A  R O D A D A !
            >> O
            O F O I  O  V E N C E D O R  D A  R O D A D A !
        """
        print(20 * '*')
        print(f" {resultado}  F O I  O  V E N C E D O R  D A  R O D A D A !")
        print(20 * '*')

    def mostra_empate(self):
        """
        Exibe uma mensagem informando que a partida deu velha

        Returns:
            Não retorna nada
        
        Exemplo:
            -=-=-=-=-=-=-=-=- D E U  V E L H A -=-=-=-=-=-=-=-=-=-=
        """
        print(45 * '#')
        print('-=-=-=-=-=-=-=-=- D E U  V E L H A -=-=-=-=-=-=-=-=-=-=')
        print(45 * '#')
