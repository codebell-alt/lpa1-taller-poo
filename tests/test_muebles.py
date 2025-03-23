# pruebas unitarias utilizando pytest
import pytest
from muebleria.muebles import Silla, Mesa, Armario

def test_silla():
    silla = Silla("Madera", 50, True)
    assert silla.calcular_precio_final() == pytest.approx(55)  

def test_mesa():
    mesa = Mesa("Metal", 100, "Grande")
    assert mesa.calcular_precio_final() == pytest.approx(120)

def test_armario():
    armario = Armario("Plástico", 200, 2)
    assert armario.calcular_precio_final() == pytest.approx(230)
