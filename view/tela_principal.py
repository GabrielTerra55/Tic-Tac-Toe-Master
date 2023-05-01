class TelaPrincipal:
    def abre_tela(self):
        """
        Exibe o menu de opções e recolhe a opção escolhida do usuario

        Returns:
            str: numero relativo a opção
        
        Exemplo:
            >> 5 Trata se a opção não corresponde as existente
            1
            >> 1
            1
        """
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
        """
        Exibe uma mensagem de encerramento do sistema

        Returns:
            Não retorna nada
        """
        print(5 * '-', 'Jogo encerrado', 5 * '-')

    def opcao_invalida(self):
        """
        Exibe uma mensagem informando que a opção escolhida não é valida

        Returns:
            Não retorna nada
        """
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')
