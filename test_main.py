from data.funcionalidades import *
def test_es_bisiesto():
    assert es_bisiesto(2020) == True
    assert es_bisiesto(2021) == False
    assert es_bisiesto(2000) == True

def test_validar_fecha():
    assert validar_fecha("29/02/2020") == True
    assert validar_fecha("29/02/2021") == False
    assert validar_fecha("31/04/2021") == False
    assert validar_fecha("31/12/2021") == True