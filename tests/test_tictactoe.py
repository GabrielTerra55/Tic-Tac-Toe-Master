from model.tictactoe import TicTacToe
import pytest
from pytest import mark



class TestClassModel:
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

    def test_manipulacao_de_jogada(self):
        #given
        x = 1
        resposta = 1
        #when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.jogada += x
        resultado = test_tic_tac_toe.jogada
        #than
        assert resultado == resposta
    
    def test_manipulacao_de_jogador(self):
        # given
        valor = 1
        resposta = 2
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.jogador += valor
        resultado = test_tic_tac_toe.jogador
        # than
        assert resultado == resposta
    
    def test_manipula_ganhador(self):
        # given
        valor = 'X'
        resposta = 'X'
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.ganhador = valor
        resultado = test_tic_tac_toe.ganhador
        # than
        assert resultado == resposta
