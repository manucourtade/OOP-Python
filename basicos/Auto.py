class Vehiculo:
    def __init__(self, marca, velocidad_maxima):
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima

class Auto(Vehiculo):
    def __init__(self, cant_puertas, marca, velocidad_maxima):
        super().__init__(marca, velocidad_maxima)
        self.cant_puertas = cant_puertas

    def describir(self):
        print(f"Marca :{self.marca} - Velocidad Máxima: {self.velocidad_maxima} km/h - Cantidad de Puertas: {self.cant_puertas}")

a1 = Auto(4, "Toyota", 180)
a1.describir()
