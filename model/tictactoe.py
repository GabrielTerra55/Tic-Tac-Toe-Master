class TicTacToe:
    def __init__(self):
        self.__cerquilha = [[0 for j in range(3)] for i in range(3)]
        self.__placar_x = 0
        self.__placar_o = 0

    @property
    def cerquilha(self):
        return self.__cerquilha

    @cerquilha.setter
    def cerquilha(self, cerquilha):
        self.__cerquilha = cerquilha

    @property
    def placar_x(self):
        return self.__placar_x

    @placar_x.setter
    def placar_x(self, placar_x):
        if not isinstance(placar_x, int):
            raise TypeError("somente numeros inteiros são validos")
        self.__placar_x = placar_x

    @property
    def placar_o(self):
        return self.__placar_o

    @placar_o.setter
    def placar_o(self, placar_o):
        if not isinstance(placar_o, int):
            raise TypeError("somente numeros inteiros são validos")
        self.__placar_o = placar_o
