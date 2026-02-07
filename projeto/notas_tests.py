import pytest
from notas import (
    validar_nota,
    calcular_media,
    obter_situacao,
    calcular_estatisticas,
    normalizar_notas
)


class TestValidarNota:
    
    def test_nota_valida_zero(self):
        assert validar_nota(0) == True
    
    def test_nota_valida_meio(self):
        assert validar_nota(5) == True
    
    def test_nota_valida_maxima(self):
        assert validar_nota(10) == True
    
    def test_nota_invalida_negativa(self):
        assert validar_nota(-1) == False
    
    def test_nota_invalida_acima_limite(self):
        assert validar_nota(11) == False


class TestCalcularMedia:
    
    def test_media_notas_iguais(self):
        assert calcular_media([5, 5, 5, 5]) == 5.0
    
    def test_media_notas_diferentes(self):
        assert calcular_media([0, 10]) == 5.0
    
    def test_media_uma_nota(self):
        assert calcular_media([7.5]) == 7.5
    
    def test_media_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])
    
    def test_media_tres_notas(self):
        assert calcular_media([6, 7, 8]) == 7.0


class TestObterSituacao:
    
    def test_aprovado_nota_minima(self):
        assert obter_situacao(7.0) == "Aprovado"
    
    def test_aprovado_nota_alta(self):
        assert obter_situacao(9.5) == "Aprovado"
    
    def test_recuperacao_nota_minima(self):
        assert obter_situacao(5.0) == "Recuperacao"
    
    def test_recuperacao_nota_media(self):
        assert obter_situacao(6.5) == "Recuperacao"
    
    def test_reprovado_nota_baixa(self):
        assert obter_situacao(4.9) == "Reprovado"
    
    def test_reprovado_nota_zero(self):
        assert obter_situacao(0) == "Reprovado"
    
    def test_situacao_media_invalida(self):
        with pytest.raises(ValueError):
            obter_situacao(-1)
    
    def test_situacao_media_acima_limite(self):
        with pytest.raises(ValueError):
            obter_situacao(11)


class TestCalcularEstatisticas:
    
    def test_estatisticas_todos_aprovados(self):
        resultado = calcular_estatisticas([8, 9, 10])
        assert resultado["aprovados"] == 3
        assert resultado["reprovados"] == 0
        assert resultado["recuperacao"] == 0
    
    def test_estatisticas_misto(self):
        resultado = calcular_estatisticas([3, 6, 8])
        assert resultado["aprovados"] == 1
        assert resultado["recuperacao"] == 1
        assert resultado["reprovados"] == 1
    
    def test_estatisticas_maior_menor(self):
        resultado = calcular_estatisticas([2, 5, 10])
        assert resultado["maior"] == 10
        assert resultado["menor"] == 2
    
    def test_estatisticas_media_correta(self):
        resultado = calcular_estatisticas([5, 5, 5])
        assert resultado["media"] == 5.0


class TestNormalizarNotas:
    
    def test_normalizar_escala_20(self):
        assert normalizar_notas([10, 20], 20) == [5.0, 10.0]
    
    def test_normalizar_escala_100(self):
        assert normalizar_notas([50, 100], 100) == [5.0, 10.0]
    
    def test_normalizar_lista_vazia(self):
        assert normalizar_notas([]) == []
    
    def test_normalizar_nota_maxima_invalida(self):
        with pytest.raises(ValueError):
            normalizar_notas([5, 10], 0)