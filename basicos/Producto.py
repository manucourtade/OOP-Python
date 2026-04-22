class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor == "":
            raise ValueError("No puede ingresar una cadena vacia")
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("No puede ser numeros negativos")
        self._precio = valor


p1 = Producto("Laptop", 250000)
print(p1)
p1.nombre = ""
p1.precio = -10000
print(p1.nombre)
