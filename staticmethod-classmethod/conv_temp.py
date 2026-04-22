class Temperatura:

    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def es_valida(valor):
        return valor > -273.15

    @classmethod
    def desde_fahrenheit(cls, f):
        c = (f - 32) * 5 / 9
        return cls(c)

    @classmethod
    def desde_kelvin(cls, k):
        c = k - 273.15
        return cls(c)

    def __str__(self):
        return f"{self.celsius:.2f}°C"


celcius = Temperatura(45)
from_k = celcius.desde_kelvin(123)
from_f = celcius.desde_fahrenheit(65)
print(celcius)
print(from_k)
print(from_f)
