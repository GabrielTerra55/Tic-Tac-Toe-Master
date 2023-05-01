class TicTacToe:
    def __init__(self):
        self.__cerquilha = [[0 for j in range(3)] for i in range(3)]
        self.__jogada = 0
        self.__jogador = 1
        self.__ganhador = None

    @property
    def cerquilha(self):
        return self.__cerquilha

    @cerquilha.setter
    def cerquilha(self, cerquilha):
        self.__cerquilha = cerquilha

    @property
    def jogada(self):
        return self.__jogada

    @jogada.setter
    def jogada(self, jogada):
        if not isinstance(jogada, int):
            raise ValueError ("somente numeros inteiros são validos")
        self.__jogada = jogada

    @property
    def jogador(self):
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador):
        if not isinstance(jogador, int):
            raise ValueError('somente numeros inteiros são validos')
        self.__jogador = jogador

    @property
    def ganhador(self):
        return self.__ganhador

    @ganhador.setter
    def ganhador(self, ganhador):
        self.__ganhador = ganhador

    def __str__(self):
        return f'{self.cerquilha} {self.ganhador}'