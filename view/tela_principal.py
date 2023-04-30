class TelaPrincipal:
    def abre_tela(self):
        print("-------- Tic-Tac-Toe ---------")
        print("Escolha uma opção")
        print("1 - Jogar")
        print("0 - Encerrar")

        opcao = input("Escolha uma opção: ")
        while opcao != '0' and opcao != '1':
            self.opcao_invalida()
            opcao = input("Escolha uma opção: ")
        opcao = int(opcao)
        return opcao

    def sistema_encerrado(self):
        print(5 * '-', 'Jogo encerrado', 5 * '-')

    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')
