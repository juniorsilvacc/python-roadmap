from functions import sub, length, validate_email, somar_lista, encontrar_valor
import pytest

def test_sub_and_length():
    assert sub(3, 2) == 1
    assert length([1, 2, 3]) == 3

def test_validate_email():
    assert validate_email('juniorsilva@hotmail.com') is True
    assert validate_email('hotmail.com') is False

def test_somar_lista():
    assert somar_lista([1, 2, 3]) == 6
    assert somar_lista([10.5, 10.5]) == 21.0
    assert somar_lista([]) == 0

    with pytest.raises(ValueError):
        somar_lista([1, 2, 'a'])

def test_encontrar_valor():
    dicionario = {'a': 1, 'b': 2, 'c': 3}
    assert encontrar_valor(dicionario, 'a') == 1
    assert encontrar_valor(dicionario, 'b') == 2
    assert encontrar_valor(dicionario, 'd') is None

    with pytest.raises(ValueError):
        encontrar_valor('não é um dicionário', 'a')