class TelaTicTacToe:
    def jogada(self, tabela):
        self.mostra_tabela(tabela)

    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UMA OPÇÃO VÁLIDA!')
        print(20 * '*')

    def mostra_tabela(self, tabela):
        for i in range(0, 2):
            for c in range(0, 2):
                print(f'[{tabela [i][c]}:^3]', end='')
            print()


tela = TelaTicTacToe()
tela.jogada([[0 for j in range(3)] for i in range(3)])
