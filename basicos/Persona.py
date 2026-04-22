class Persona:
    def __init__(self,  nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre} {self.apellido} y tengo {self.edad} años.")

    def es_mayor_de_edad(self):
        return self.edad >= 18
    
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def es_cuadrado(self):
        return self.base == self.altura
    

class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, monto):
        self.saldo+= monto
        return self.saldo
    
    def extraer(self, monto):
        self.saldo-= monto
        return self.saldo
    
    def ver_saldo(self):
        print(f"Saldo actual: {self.saldo}")

class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, cantidad_puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.cantidad_puertas = cantidad_puertas
    
    def describirse(self):
        print(f"Marca: {self.marca} {self.modelo} - {self.velocidad_maxima} - Cantidad puertas: {self.cantidad_puertas}")

class Moto(Vehiculo):
    def __init__(self, marca,modelo,velocidad_maxima, tipo):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo

    def describirse(self):
        print(f"Marca: {self.marca} {self.modelo} - {self.velocidad_maxima} - Tipo: {self.tipo}")

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)
    
    def promedio(self):
        return sum(self.notas) / len(self.notas)
        
    
    def __str__(self):
        return f'Estudiante: {self.nombre} - Notas: {self.notas} - Promedio: {self.promedio()}'
    
class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        estado = "disponible" if self.disponible else "prestado"
        return f'"{self.titulo}" de {self.autor} — {estado}'


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_por_autor(self, autor):
        resultado = []
        for libro in self.libros:
            if libro.autor == autor:
                resultado.append(libro)
        return resultado

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f'"{titulo}" prestado con éxito.')
                return
        print(f'"{titulo}" no está disponible o no existe.')

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                print(f'"{titulo}" devuelto con éxito.')
                return
        print(f'"{titulo}" no estaba prestado o no existe.')


# Prueba
b = Biblioteca()
b.agregar_libro(Libro("Cien años de soledad", "García Márquez"))
b.agregar_libro(Libro("El amor en tiempos de cólera", "García Márquez"))
b.agregar_libro(Libro("1984", "Orwell"))

b.prestar_libro("1984")
b.prestar_libro("1984")  # intento duplicado

for libro in b.buscar_por_autor("García Márquez"):
    print(libro)

b.devolver_libro("1984")