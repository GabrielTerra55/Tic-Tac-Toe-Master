class TicTacToe:
    def __init__(self):
        self.__cerquilha = [[0 for j in range(3)] for i in range(3)]
        self.__pontuacao_x = 0
        self.__pontuacao_o = 0
        self.__jogadas_x = 0
        self.__jogadas_o = 0

    @property
    def cerquilha(self):
        return self.__cerquilha

    @cerquilha.setter
    def cerquilha(self, cerquilha):
        self.__cerquilha = cerquilha

    @property
    def pontuacao_x(self):
        return self.__pontuacao_x

    @pontuacao_x.setter
    def pontuacao_x(self, pontuacao_x):
        if not isinstance(pontuacao_x, int):
            raise TypeError("somente numeros inteiros são validos")
        self.__pontuacao_x = pontuacao_x

    @property
    def pontuacao_o(self):
        return self.__pontuacao_o

    @pontuacao_o.setter
    def pontuacao_o(self, pontuacao_o):
        if not isinstance(pontuacao_o, int):
            raise TypeError("somente numeros inteiros são validos")
        self.__pontuacao_o = pontuacao_o

    @property
    def jogadas_x(self):
        return self.__jogadas_x
    
    @jogadas_x.setter
    def jogadas_x(self, jogadas_x):
        self.__jogadas_x = jogadas_x
    
    @property
    def jogadas_o(self):
        return self.__jogadas_o 
    
    @jogadas_o.setter
    def jogadas_o(self, jogadas_o):
        self.__jogadas_o = jogadas_o