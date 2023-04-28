from model.tictactoe import TicTacToe
import pytest
from pytest import mark
'''
 Metodologia Given-When-Then :
    . e uma metodologia agil para o desenvolvimento de testes

. given -- Dado(contexto)...
. when -- Quando(acao)...
. then -- entao(desfecho)...
'''


class TestClassModel:
    def test_de_manipulacao_do_atributo_X(self):
        # given
        x = 1
        receber_x = 1
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.pontuacao_x = x
        resultado = test_tic_tac_toe.pontuacao_x
        # than
        assert resultado == receber_x

    def test_de_manipulacao_do_atributo_O(self):
        # given
        o = 2
        receber_o = 2
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.pontuacao_o = o
        resultado = test_tic_tac_toe.pontuacao_o
        # than
        assert resultado == receber_o

    def test_de_manipulação_do_atrbuto_cerquilha(self):
        # given
        cerquilha = [[0, 0, 0], [0, 'X', 0], [0, 0, 0]]
        receber = [[0, 0, 0], [0, 'X', 0], [0, 0, 0]]
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.cerquilha = cerquilha
        resultado = test_tic_tac_toe.cerquilha
        # than
        assert resultado == cerquilha

    def test_tentando_instanciar_uma_string_em_pontuacao_x(self):
        with pytest.raises(TypeError):
            # given
            x = 'X'
            # when
            test_tic_tac_toe = TicTacToe()
            resultado = test_tic_tac_toe.pontuacao_x = x
            # than
            assert resultado

    def test_tentando_instanciar_uma_string_em_pontuacao_o(self):
        with pytest.raises(TypeError):
            # given
            o = 'O'
            # when
            test_tic_tac_toe = TicTacToe()
            resultado = test_tic_tac_toe.pontuacao_o = o
            # than
            assert resultado

    def test_testando_manipulacao_de_jogadas_x(self):
        #given
        x = 1
        resposta_x = 1
        #when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.jogadas_x += x
        resultado = test_tic_tac_toe.jogadas_x
        #than
        assert resultado == resposta_x
    
    def test_testando_manipulacao_de_jogadas_o(self):
        #given
        o = 1
        resposta_o = 1
        #when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.jogadas_o += o
        resultado = test_tic_tac_toe.jogadas_o
        #than
        assert resultado == resposta_o