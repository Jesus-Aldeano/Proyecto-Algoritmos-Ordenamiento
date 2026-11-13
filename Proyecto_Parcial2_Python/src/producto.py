from dataclasses import dataclass

@dataclass
class Producto:
    """Representa un producto del catálogo de la tienda en línea."""
    id: int
    nombre: str
    precio: float
    categoria: str
    stock: int
    calificacionPromedio: float

    def __str__(self):
        return (f"Producto(id={self.id}, nombre='{self.nombre}', "
                f"precio=${self.precio:.2f}, categoria='{self.categoria}', "
                f"stock={self.stock}, calificacion={self.calificacionPromedio:.1f})")
