import math


class Figura:
    def area(self):
        return 0


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2

    def __str__(self):
        return f"Figura: Circulo - Radio: {self.radio:.2f} - Area: {self.area():.2f}"


class Triangulo(Figura):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return (self.b * self.h) / 2

    def __str__(self):
        return f"Figura: Triangulo - Base: {self.b:.2f} - Altura: {self.h:.2f} - Area: {self.area():.2f}"


class Rectangulo(Figura):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

    def __str__(self):
        return f"Figura: Rectangulo - Base: {self.b:.2f} - Altura: {self.h:.2f} - Area: {self.area():.2f}"


def calcular_areas(figuras):
    for figura in figuras:
        print(figura.area())


if __name__ == "__main__":
    circulo = Circulo(5)
    triangulo = Triangulo(4, 6)
    rectangulo = Rectangulo(3, 7)

    figuras = [circulo, triangulo, rectangulo]
    calcular_areas(figuras)
    print(circulo)
    print(triangulo)
    print(rectangulo)
