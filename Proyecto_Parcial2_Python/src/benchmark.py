import time
import random
import statistics
from ordenamientos import merge_sort, quick_sort, heap_sort
from busquedas import busqueda_binaria_por_id, busqueda_lineal_por_subcadena
from generador import generar_productos

ALGORITMOS = {
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
}

def medir_ordenamientos(productos, repeticiones=1000):
    """Promedio por ordenamiento, medido sobre copias idénticas de 50 productos."""
    criterios = {
        "Precio ascendente": lambda p: p.precio,
        "Calificación descendente": lambda p: -p.calificacionPromedio,
    }
    resultados = []
    for criterio, clave in criterios.items():
        for nombre, algoritmo in ALGORITMOS.items():
            muestras = []
            for _ in range(repeticiones):
                copia = productos[:]
                inicio = time.perf_counter_ns()
                ordenados = algoritmo(copia, clave)
                fin = time.perf_counter_ns()
                muestras.append(fin - inicio)
                # Verificación de orden en cada repetición.
                claves = [clave(p) for p in ordenados]
                assert claves == sorted(claves)
            resultados.append({
                "criterio": criterio,
                "algoritmo": nombre,
                "promedio_us": statistics.mean(muestras) / 1000,
                "mediana_us": statistics.median(muestras) / 1000,
                "repeticiones": repeticiones
            })
    return resultados

def _promedio_lote(funcion, repeticiones=1000):
    muestras = []
    for _ in range(repeticiones):
        inicio = time.perf_counter_ns()
        funcion()
        muestras.append(time.perf_counter_ns() - inicio)
    return statistics.mean(muestras) / 1000  # microsegundos por lote de 10 consultas

def medir_busquedas(productos, semilla=2026):
    rng = random.Random(semilla)
    por_id = sorted(productos, key=lambda p: p.id)
    ids_existentes = rng.sample([p.id for p in por_id], 10)
    ids_inexistentes = rng.sample(range(1001, 5000), 10)

    encontrados = [busqueda_binaria_por_id(por_id, x) for x in ids_existentes]
    no_encontrados = [busqueda_binaria_por_id(por_id, x) for x in ids_inexistentes]
    assert all(encontrados)
    assert all(x is None for x in no_encontrados)
    tiempo_existen_us = _promedio_lote(lambda: [busqueda_binaria_por_id(por_id, x) for x in ids_existentes])
    tiempo_no_existen_us = _promedio_lote(lambda: [busqueda_binaria_por_id(por_id, x) for x in ids_inexistentes])

    # Consultas que se sabe que aparecen en los nombres y consultas sin coincidencias.
    consultas_positivas = ["pro", "premium", "clásico", "digital", "compacto",
                           "ergonómico", "camisa", "libro", "mesa", "audífonos"]
    consultas_negativas = ["xyz_no_existe", "qwerty", "sin_coincidencia_01",
                           "articulo_inexistente", "zzzz", "producto_fantasma",
                           "no_hay_resultado", "abc999", "inexistente", "nada_que_ver"]
    # Asegurar que cada positiva produzca al menos un resultado: si no, usar tokens garantizados.
    positivos = []
    for q in consultas_positivas:
        if not busqueda_lineal_por_subcadena(productos, q):
            q = next(palabra for producto in productos for palabra in producto.nombre.split()
                     if busqueda_lineal_por_subcadena(productos, palabra))
        positivos.append(q)

    resultados_positivos = [busqueda_lineal_por_subcadena(productos, q) for q in positivos]
    resultados_negativos = [busqueda_lineal_por_subcadena(productos, q) for q in consultas_negativas]
    assert all(resultados_positivos)
    assert all(not r for r in resultados_negativos)
    tiempo_nombres_si_us = _promedio_lote(lambda: [busqueda_lineal_por_subcadena(productos, q) for q in positivos])
    tiempo_nombres_no_us = _promedio_lote(lambda: [busqueda_lineal_por_subcadena(productos, q) for q in consultas_negativas])

    return {
        "ids_existentes": ids_existentes,
        "ids_inexistentes": ids_inexistentes,
        "binaria_10_existentes_us": tiempo_existen_us,
        "binaria_10_inexistentes_us": tiempo_no_existen_us,
        "consultas_nombres_positivas": positivos,
        "consultas_nombres_negativas": consultas_negativas,
        "lineal_10_positivas_us": tiempo_nombres_si_us,
        "lineal_10_negativas_us": tiempo_nombres_no_us,
        "repeticiones_por_lote": 1000,
    }
