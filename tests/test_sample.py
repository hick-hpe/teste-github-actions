"""
Teste validar_placa
"""
from ex import validar_placa

def test_validar_placa():
    # válidas
    assert validar_placa("ABC1D23") == True
    assert validar_placa("XYZ9Z99") == True
    assert validar_placa("AAA0A00") == True
    assert validar_placa("BBB1C45") == True
    assert validar_placa("MNO2X78") == True
    assert validar_placa("QWE3Z12") == True
    assert validar_placa("RTY4B34") == True
    assert validar_placa("UIO5C56") == True
    assert validar_placa("PAS6D78") == True
    assert validar_placa("LKJ7E90") == True

    # inválidas
    assert validar_placa("AB12C34") == False
    assert validar_placa("ABCDE12") == False
    assert validar_placa("A1B2C34") == False
    assert validar_placa("1234ABC") == False
    assert validar_placa("AB1CD23") == False
    assert validar_placa("ABC1234") == False
    assert validar_placa("ABCD123") == False
    assert validar_placa("abc1d23") == False
    assert validar_placa("A!C1D23") == False
    assert validar_placa("") == False
