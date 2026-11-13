import random
from producto import Producto

CATEGORIAS = ["Electrónica", "Ropa", "Libros", "Hogar", "Deportes"]
NOMBRES = {
    "Electrónica": ["Audífonos", "Teclado", "Mouse", "Monitor", "Cámara", "Parlante", "Tablet"],
    "Ropa": ["Camisa", "Pantalón", "Chaqueta", "Vestido", "Sudadera", "Zapatos", "Gorra"],
    "Libros": ["Libro de Python", "Novela", "Atlas", "Manual de datos", "Diccionario", "Biografía"],
    "Hogar": ["Lámpara", "Silla", "Mesa", "Cafetera", "Almohada", "Organizador", "Licuadora"],
    "Deportes": ["Balón", "Mancuernas", "Bicicleta", "Raqueta", "Botella deportiva", "Colchoneta"]
}
ADJETIVOS = ["Básico", "Premium", "Compacto", "Pro", "Clásico", "Digital", "Ergonómico"]

def generar_productos(cantidad=50, semilla=2026):
    """Genera productos coherentes y reproducibles; los ID son únicos."""
    rng = random.Random(semilla)
    productos = []
    for identificador in range(1, cantidad + 1):
        categoria = rng.choice(CATEGORIAS)
        nombre = f"{rng.choice(NOMBRES[categoria])} {rng.choice(ADJETIVOS)}"
        precio = round(rng.uniform(4.99, 999.99), 2)
        stock = rng.randint(0, 150)
        calificacion = round(rng.uniform(1.0, 5.0), 1)
        productos.append(Producto(
            id=identificador, nombre=nombre, precio=precio,
            categoria=categoria, stock=stock,
            calificacionPromedio=calificacion
        ))
    return productos
