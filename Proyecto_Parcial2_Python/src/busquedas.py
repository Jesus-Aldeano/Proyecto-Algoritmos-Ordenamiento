def busqueda_binaria_por_id(productos_ordenados, id_buscado):
    """Devuelve el Producto con ese ID o None. Requiere lista ordenada por ID."""
    izquierda, derecha = 0, len(productos_ordenados) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = productos_ordenados[medio].id
        if actual == id_buscado:
            return productos_ordenados[medio]
        if actual < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

def busqueda_lineal_por_subcadena(productos, subcadena):
    """Busca sin distinguir mayúsculas/minúsculas; devuelve todas las coincidencias."""
    termino = subcadena.casefold()
    return [p for p in productos if termino in p.nombre.casefold()]
