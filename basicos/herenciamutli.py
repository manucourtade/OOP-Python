class SalarioInvalidoError(Exception):
    pass


class Trabajador:
    def __init__(self, salario):
        self.salario = salario  # pasa por el setter

    def trabajar(self):
        print("Estoy trabajando")

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise SalarioInvalidoError("No puede ingresar salarios negativos")
        self._salario = valor


class Estudiante:
    def __init__(self, promedio):
        self._promedio = promedio

    def estudiar(self):
        print("Estoy estudiando")


class Becario(Trabajador, Estudiante):
    def __init__(self, salario, promedio):
        Trabajador.__init__(self, salario)
        Estudiante.__init__(self, promedio)

    def descripcion(self):
        print(f"Promedio: {self._promedio} - Salario: {self.salario}")


try:
    b1 = Becario(-500, 8)
except SalarioInvalidoError as e:
    print(f"Error: {e}")

try:
    b2 = Becario(150000, 9)
    b2.descripcion()
    b2.trabajar()
    b2.estudiar()
except SalarioInvalidoError as e:
    print(f"Error: {e}")
