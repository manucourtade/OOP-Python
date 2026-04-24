from dataclasses import dataclass
from .excepciones import *


@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int

    def __post_init__(self):
        if not self.nombre.strip():
            raise NombreInvalidoError("No puede ingresar productos sin nombre!")
        if self.precio <= 0:
            raise PrecioInvalidoError(
                "No ingrese negativos y no regale su producto por favor!"
            )
        if self.stock < 0:
            raise StockInvalidoError("No ingrese cantidad negativas!")
