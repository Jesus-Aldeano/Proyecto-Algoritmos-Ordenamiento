import matplotlib.pyplot as plt

def crear_graficos(ordenamientos, busquedas, carpeta):
    nombres = ["Merge Sort", "Quick Sort", "Heap Sort"]
    criterios = ["Precio ascendente", "Calificación descendente"]
    for criterio in criterios:
        filas = [r for r in ordenamientos if r["criterio"] == criterio]
        valores = [next(r["promedio_us"] for r in filas if r["algoritmo"] == n) for n in nombres]
        plt.figure()
        plt.bar(nombres, valores)
        plt.title(f"Tiempo promedio: {criterio}")
        plt.ylabel("Microsegundos por ordenamiento")
        plt.xlabel("Algoritmo")
        plt.tight_layout()
        plt.savefig(f"{carpeta}/ordenamiento_{'precio' if criterio.startswith('Precio') else 'calificacion'}.png", dpi=160)
        plt.close()

    etiquetas = ["Binaria: ID existe", "Binaria: ID no existe",
                 "Lineal: nombre coincide", "Lineal: sin coincidencia"]
    valores = [busquedas["binaria_10_existentes_us"], busquedas["binaria_10_inexistentes_us"],
               busquedas["lineal_10_positivas_us"], busquedas["lineal_10_negativas_us"]]
    plt.figure()
    plt.bar(etiquetas, valores)
    plt.title("Tiempo total de 10 búsquedas por escenario")
    plt.ylabel("Microsegundos")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(f"{carpeta}/busquedas.png", dpi=160)
    plt.close()
