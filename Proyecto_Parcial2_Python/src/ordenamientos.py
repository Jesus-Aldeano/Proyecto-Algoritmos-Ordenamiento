"""Tres algoritmos genéricos de ordenamiento para objetos Producto."""

def merge_sort(datos, clave):
    if len(datos) <= 1:
        return datos[:]
    medio = len(datos) // 2
    izquierda = merge_sort(datos[:medio], clave)
    derecha = merge_sort(datos[medio:], clave)
    resultado, i, j = [], 0, 0
    while i < len(izquierda) and j < len(derecha):
        # <= conserva el orden relativo en caso de empate (estable).
        if clave(izquierda[i]) <= clave(derecha[j]):
            resultado.append(izquierda[i]); i += 1
        else:
            resultado.append(derecha[j]); j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def quick_sort(datos, clave):
    """Quick Sort con partición de Lomuto y pivote final."""
    arreglo = datos[:]
    def ordenar(inicio, fin):
        if inicio < fin:
            pivote = clave(arreglo[fin])
            i = inicio - 1
            for j in range(inicio, fin):
                if clave(arreglo[j]) <= pivote:
                    i += 1
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
            pos = i + 1
            arreglo[pos], arreglo[fin] = arreglo[fin], arreglo[pos]
            ordenar(inicio, pos - 1)
            ordenar(pos + 1, fin)
    ordenar(0, len(arreglo) - 1)
    return arreglo

def heap_sort(datos, clave):
    """Heap Sort ascendente; max-heap con hundimiento iterativo."""
    arreglo = datos[:]
    n = len(arreglo)
    def hundir(tam, raiz):
        while True:
            mayor = raiz
            izq, der = 2 * raiz + 1, 2 * raiz + 2
            if izq < tam and clave(arreglo[izq]) > clave(arreglo[mayor]):
                mayor = izq
            if der < tam and clave(arreglo[der]) > clave(arreglo[mayor]):
                mayor = der
            if mayor == raiz:
                break
            arreglo[raiz], arreglo[mayor] = arreglo[mayor], arreglo[raiz]
            raiz = mayor
    for i in range(n // 2 - 1, -1, -1):
        hundir(n, i)
    for fin in range(n - 1, 0, -1):
        arreglo[0], arreglo[fin] = arreglo[fin], arreglo[0]
        hundir(fin, 0)
    return arreglo
