class VelocidadInvalidaError(Exception):
    pass


class Motor:
    def __init__(self, cilindrada):
        self._cilindrada = cilindrada

    def encender(self):
        print("Estoy encedido")


class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self._marca = marca
        self.velocidad_max = velocidad_max

    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor):
        if valor < 0:
            raise VelocidadInvalidaError("No ingresar velocidades negativas")
        self._velocidad_max = valor

    def describirse(self):
        return f"Marca: {self._marca} - Velocidad max: {self.velocidad_max}"


class Auto(Motor, Vehiculo):
    def __init__(self, cilindrada, marca, velocidad_max, puertas):
        Motor.__init__(self, cilindrada)
        Vehiculo.__init__(self, marca, velocidad_max)
        self.puertas = puertas

    def describirse(self):
        print(
            f"{Vehiculo.describirse(self)} - Cilindradas: {self._cilindrada} - Puertas: {self.puertas}"
        )

    def __str__(self):
        return f"Marca: {self._marca} - CC: {self._cilindrada} - Puertas: {self.puertas} - Vel_MAX: {self.velocidad_max}"


try:
    a1 = Auto(1600, "Peugeot 208", 200, 4)
    a1.encender()
    print(a1)
except VelocidadInvalidaError as e:
    print(f"Error: {e}")
print("-" * 100)
try:
    a1 = Auto(1600, "Peugeot 208", -200, 4)
    a1.encender()
    a1.describirse()

except VelocidadInvalidaError as e:
    print(f"Error: {e}")
