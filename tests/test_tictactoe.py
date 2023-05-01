import pytest
from pytest import mark

from model.tictactoe import TicTacToe
from controller.controller_principal import ControllerPrincipal



class TestClassModelTicTacToe:
    def test_de_manipulação_do_atrbuto_cerquilha_deve_retonar_cerquilha_alterada(self):
        # given
        cerquilha = [[0, 0, 0], [0, 'X', 0], [0, 0, 0]]
        receber = [[0, 0, 0], [0, 'X', 0], [0, 0, 0]]
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.cerquilha = cerquilha
        resultado = test_tic_tac_toe.cerquilha
        # than
        assert resultado == receber

    def test_manipulacao_de_jogada_deve_retonar_1(self):
        # given
        x = 1
        resposta = 1
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.jogada += x
        resultado = test_tic_tac_toe.jogada
        # than
        assert resultado == resposta

    def test_manipulacao_de_jogador_deve_retonar_2(self):
        # given
        valor = 1
        resposta = 2
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.jogador += valor
        resultado = test_tic_tac_toe.jogador
        # than
        assert resultado == resposta

    def test_manipula_ganhador_deve_retornar_X(self):
        # given
        valor = 'X'
        resposta = 'X'
        # when
        test_tic_tac_toe = TicTacToe()
        test_tic_tac_toe.ganhador = valor
        resultado = test_tic_tac_toe.ganhador
        # than
        assert resultado == resposta

    def test_inserindo_valor_indevido_em_jogador_deve_retornar_valuerror(self):
        with pytest.raises(ValueError):
            # given
            entrada = '5'
            # when
            test_tic_tac_toe = TicTacToe()
            resultado = test_tic_tac_toe.jogador = entrada
            # than
            assert resultado

    def test_inserindo_valor_indevido_em_jogada_deve_retornar_valuerror(self):
        with pytest.raises(ValueError):
            # given
            entrada = '8'
            # when
            test_tic_tac_toe = TicTacToe()
            resultado = test_tic_tac_toe.jogada = entrada
            # than
            assert resultado

    class TestClassControllerTicTacToe:
        def test_inserindo_uma_posição_relativa_deve_retonar_posicao_absoluta(self):
            #given
            entrada = 5
            esperado = '11'
            # when
            test_controller_tic_tac_toe = ControllerPrincipal()
            resultado = test_controller_tic_tac_toe.controller_tictactoe.converter_em_posicao_real(entrada)
            #than
            assert resultado == esperado
        
        def test_inserindo_uma_posição_deve_retonar_a_mesma_posicao(self):
            # given
            entrada = '5'
            esperado = '5'
            # when
            test_controller_tic_tac_toe = ControllerPrincipal()
            resultado = test_controller_tic_tac_toe.controller_tictactoe.verificar_posicao(entrada, test_controller_tic_tac_toe.controller_tictactoe.tic_tac_toe.cerquilha)
            # than
            assert resultado == esperado

        def test_verifica_se_a_jogada_e_maior_que_5_deve_retornar_true(self):
            # given
            entrada = 8
            esperado = True
            # when
            test_controller_tic_tac_toe = ControllerPrincipal()
            resultado = test_controller_tic_tac_toe.controller_tictactoe.jogada_maior_que_5(
                entrada)
            # than
            assert resultado == esperado
        
        def test_verifica_retorna_o_jogador_x_(self):
            # given
            entrada = 3
            esperado = 'X'
            # when
            test_controller_tic_tac_toe = ControllerPrincipal()
            resultado = test_controller_tic_tac_toe.controller_tictactoe.tic_tac_toe.jogador = 3
            resultado = test_controller_tic_tac_toe.controller_tictactoe.definir_jogador()
            # than
            assert resultado == esperado
