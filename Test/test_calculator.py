import pytest
from App.calculator import AvanaCalculator


@pytest.fixture
def calc():
    return AvanaCalculator()


# ─── CASOS EXITOSOS ───────────────────────────────────────

class TestCasosExitosos:

    def test_descuento_efectivo(self, calc):
        """Efectivo aplica 20% de descuento"""
        r = calc.calcular(100000, "efectivo")
        assert r["precio_final"] == 80000.0
        assert r["porcentaje"] == 20.0

    def test_descuento_transferencia(self, calc):
        """Transferencia aplica 5% de descuento"""
        r = calc.calcular(100000, "transferencia")
        assert r["precio_final"] == 95000.0
        assert r["porcentaje"] == 5.0

    def test_sin_descuento_tarjeta(self, calc):
        """Tarjeta no aplica descuento"""
        r = calc.calcular(100000, "tarjeta")
        assert r["precio_final"] == 100000.0
        assert r["porcentaje"] == 0.0


# ─── CASOS DE ERROR ───────────────────────────────────────

class TestCasosDeError:

    def test_precio_negativo(self, calc):
        """Precio negativo debe lanzar ValueError"""
        with pytest.raises(ValueError):
            calc.calcular(-5000, "efectivo")

    def test_precio_cero(self, calc):
        """Precio cero debe lanzar ValueError"""
        with pytest.raises(ValueError):
            calc.calcular(0, "efectivo")

    def test_medio_de_pago_invalido(self, calc):
        """Medio de pago inexistente debe lanzar ValueError"""
        with pytest.raises(ValueError):
            calc.calcular(100000, "bitcoin")


# ─── CASOS BORDE ──────────────────────────────────────────

class TestCasosBorde:

    def test_precio_minimo(self, calc):
        """El precio mínimo aceptado es 0.01"""
        r = calc.calcular(0.01, "tarjeta")
        assert r["precio_final"] == 0.01

    def test_medio_de_pago_mayusculas(self, calc):
        """El medio de pago debe aceptarse en mayúsculas"""
        r = calc.calcular(100000, "EFECTIVO")
        assert r["precio_final"] == 80000.0

    def test_precio_muy_grande(self, calc):
        """El sistema maneja precios altos correctamente"""
        r = calc.calcular(10000000, "efectivo")
        assert r["precio_final"] == 8000000.0