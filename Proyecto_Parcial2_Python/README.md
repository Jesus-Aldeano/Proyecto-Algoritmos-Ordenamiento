# Parcial 2 – Rendimiento con algoritmos de ordenamiento y búsqueda

Proyecto en Python para simular un catálogo de 50 productos de una tienda en línea, comparar Merge Sort, Quick Sort y Heap Sort, y evaluar búsquedas binarias por ID y lineales por subcadena.

## Requisitos
- Python 3.10 o superior
- matplotlib

## Instalación
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución
Desde la carpeta del proyecto:
```bash
python src/main.py
```
El programa crea en `resultados/`:
- `productos.csv`: catálogo de 50 productos.
- `tiempos_ordenamiento.csv`: mediciones de los tres algoritmos para ambos criterios.
- `tiempos_busqueda.json`: tiempos de los escenarios de búsqueda.
- `ordenamiento_precio.png`, `ordenamiento_calificacion.png`, `busquedas.png`: gráficos.

## Pruebas
```bash
python -m unittest discover -s tests -v
```

## Decisiones técnicas
- Se usa una semilla fija (2026) para que el catálogo y las pruebas sean reproducibles.
- Los algoritmos reciben una función `clave`, por lo que comparan objetos Producto por un atributo.
- La calificación descendente se obtiene usando la clave negativa `-p.calificacionPromedio`.
- Cada algoritmo recibe una copia del mismo catálogo.
- Se promedian 1,000 ejecuciones para cada ordenamiento y 1,000 lotes de 10 consultas para las búsquedas, reduciendo el ruido de mediciones muy pequeñas.
- La búsqueda binaria requiere que la lista esté ordenada previamente por ID.
- La búsqueda lineal por subcadena no distingue mayúsculas/minúsculas.

## Complejidad teórica
| Algoritmo | Mejor caso | Promedio | Peor caso | Memoria adicional |
|---|---:|---:|---:|---:|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) promedio de pila |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) auxiliar (implementación in-place) |
| Búsqueda binaria | O(1) | O(log n) | O(log n) | O(1) |
| Búsqueda lineal por subcadena | O(n·m) aprox. | O(n·m) aprox. | O(n·m) aprox. | Depende de resultados |

`n` representa la cantidad de productos y `m` la longitud del patrón de búsqueda; el costo real de comparar cadenas también depende del texto.
