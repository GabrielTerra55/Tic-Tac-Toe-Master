class TelaTicTacToe:
    def jogada(self, tabela):
        self.mostra_tabela(tabela)
        posiçõa_de_jogada = self.recolhe_Jogada
        return posiçõa_de_jogada

    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UMA OPÇÃO VÁLIDA!')
        print(20 * '*')

    def mostra_tabela(self, tabela):
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
        print(20 * '-=')
        jogada = input(' INSIRA A POSIÇÃO DA JOGADA! ')
        print(20 * '-=')
        return jogada
    
    def mostra_ganhador(self, resultado):
        print(20 * '-=')
        print(f" {resultado}  F O I  O  V E N C E D O R  D A  R O D A D A !")
        print(20 * '-=')

    def mostra_empate(self):
        print(20 * '-=')
        print('-=-=-=-=-=-=-=-=- D E U  V E L H A -=-=-=-=-=-=-=-=-=-=')
        print(20 * '-=')


'''tela = TelaTicTacToe()
tabela = [[0 for j in range(3)] for i in range(3)]
print(type(tabela[2][1]))
tela.mostra_tabela(tabela)'''
