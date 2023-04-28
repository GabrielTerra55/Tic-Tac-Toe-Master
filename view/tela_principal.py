class TelaPrincipal:
    def abre_tela(self):
        print("-------- Tic-Tac-Toe ---------")
        print("Escolha uma opção")
        print("1 - Jogar")
        print("0 - Encerrar")

        opcao = input("Escolha uma opção: ")
        while not opcao == '1' or opcao == '0':
            self.opcao_invalida()
            opcao = input("Escolha uma opção: ")

        opcao = int(opcao)
        return opcao

    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UMA OPÇÃO VÁLIDA!')
        print(20 * '*')
