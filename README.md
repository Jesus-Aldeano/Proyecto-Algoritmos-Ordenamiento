# 📦 Proyecto: Algoritmos de Ordenamiento y Búsqueda en Python

**Estudiante:** Jesús Aldeano  
**Asignatura:** Estructura de Datos  
**Proyecto:** Parcial 2  
**Lenguaje:** Python 3

---

## 📖 Descripción del proyecto

Proyecto académico enfocado en el desarrollo de un sistema de gestión de productos para una tienda en línea.

Se implementan y comparan diferentes algoritmos de ordenamiento y búsqueda, evaluando su rendimiento mediante pruebas experimentales, generación de datos aleatorios y visualizaciones gráficas.

## 🎯 Objetivos

- Modelar productos mediante programación orientada a objetos.
- Generar un catálogo de 50 productos.
- Implementar tres algoritmos de ordenamiento.
- Comparar tiempos de ejecución.
- Aplicar búsqueda binaria por identificador.
- Implementar búsqueda lineal por nombre.
- Analizar resultados mediante gráficos.

## ⚙️ Algoritmos implementados

### Ordenamiento

| Algoritmo | Complejidad promedio |
|---|---|
| Merge Sort | O(n log n) |
| Quick Sort | O(n log n) |
| Heap Sort | O(n log n) |

### Búsqueda

| Algoritmo | Complejidad |
|---|---|
| Búsqueda binaria | O(log n) |
| Búsqueda lineal | O(n) |

## 📂 Estructura del proyecto

```text
Proyecto-Algoritmos-Ordenamiento-Busqueda-Python/
│
├── README.md
├── requirements.txt
├── informe.pdf
│
├── src/
│   ├── producto.py
│   ├── generador.py
│   ├── ordenamientos.py
│   ├── busquedas.py
│   ├── benchmark.py
│   ├── visualizaciones.py
│   └── main.py
│
├── tests/
│   └── test_proyecto.py
│
└── resultados/
    ├── productos.csv
    ├── tiempos_ordenamiento.csv
    ├── tiempos_busqueda.json
    ├── ordenamiento_precio.png
    ├── ordenamiento_calificacion.png
    └── busquedas.png
```

## 🚀 Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone https://github.com/Jesus-Aldeano/Proyecto-Algoritmos-Ordenamiento-Busqueda-Python.git
```

**2. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**3. Ejecutar el programa**

```bash
python src/main.py
```

**4. Ejecutar las pruebas**

```bash
python -m unittest discover -s tests -v
```

## 📊 Resultados y visualizaciones

El proyecto genera gráficos comparativos de:

- Rendimiento por precio.
- Rendimiento por calificación.
- Comparación de búsquedas.

Los resultados experimentales se encuentran en la carpeta `resultados/`.

## 📄 Informe técnico

El informe PDF contiene la explicación del modelo de datos, metodología, resultados, gráficos, análisis de complejidad y conclusiones.

📎 **Archivo:** `informe.pdf`

## 🧪 Validación

El proyecto incluye pruebas automatizadas utilizando `unittest` para verificar la generación de productos, el ordenamiento y los algoritmos de búsqueda.

## 👨‍💻 Autor

**Jesús Aldeano**  
Estudiante de Ingeniería de Sistemas Computacionales.

---

*Proyecto académico desarrollado en Python para la aplicación práctica de estructuras de datos y análisis de rendimiento algorítmico.*
