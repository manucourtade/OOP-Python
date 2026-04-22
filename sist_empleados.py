class SueldoInvalidoError(Exception):
    pass


class EdadInvalidaError(Exception):
    pass


class NombreInvalidoError(Exception):
    pass


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if 120 < valor or valor < 0:
            raise EdadInvalidaError(
                "No puede ingresar una edad mayor a 120 ni menor a 0"
            )
        self._edad = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise NombreInvalidoError("No ingresar nombres vacios")
        self._nombre = valor


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, valor):
        if valor < 0:
            raise SueldoInvalidoError("No ingresar sueldos negativos")
        self._sueldo = valor

    def trabajar(self):
        return f"{self.nombre} esta trabajando"

    def __str__(self):
        return f"{self.nombre} - Edad: {self.edad} - Sueldo: {self.sueldo}"


class Gerente(Empleado):
    def __init__(self, nombre, edad, sueldo, departamento):
        Empleado.__init__(self, nombre, edad, sueldo)
        self.departamento = departamento

    def trabajar(self):
        return f"{self._nombre} esta gestionando el departamento {self.departamento}"

    def __str__(self):
        return f"{self.nombre} - Edad: {self.edad} - Sueldo: {self.sueldo} - Departamento: {self.departamento}"


try:
    g1 = Gerente("  Manuel", 109, -2, "RRHH")
    print(g1)
except NombreInvalidoError as e:
    print(f"Error {e}")
except SueldoInvalidoError as e:
    print(f"Error {e}")
except EdadInvalidaError as e:
    print(f"Error {e}")

try:
    g1 = Gerente("Manuel", 1119, 2500000, "RRHH")
    g1.edad = 19
    print(g1)
    print(g1.trabajar())
except NombreInvalidoError as e:
    print(f"Error {e}")
except SueldoInvalidoError as e:
    print(f"Error {e}")
except EdadInvalidaError as e:
    print(f"Error {e}")

e1 = Empleado("Carlos", 19, 25000)
print(e1)
print(e1.trabajar())
