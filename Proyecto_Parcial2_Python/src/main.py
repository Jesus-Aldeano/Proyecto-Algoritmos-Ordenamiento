import os, sys, csv, json
from pathlib import Path
from generador import generar_productos
from ordenamientos import merge_sort
from benchmark import medir_ordenamientos, medir_busquedas
from visualizaciones import crear_graficos

ROOT = Path(__file__).resolve().parents[1]
RESULTADOS = ROOT / "resultados"
RESULTADOS.mkdir(exist_ok=True)

def main():
    productos = generar_productos(50, semilla=2026)
    # Exportación del catálogo para inspección y trazabilidad.
    with open(RESULTADOS / "productos.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id","nombre","precio","categoria","stock","calificacionPromedio"])
        for p in productos:
            w.writerow([p.id,p.nombre,p.precio,p.categoria,p.stock,p.calificacionPromedio])

    ordenamientos = medir_ordenamientos(productos, repeticiones=1000)
    busquedas = medir_busquedas(productos)

    with open(RESULTADOS / "tiempos_ordenamiento.csv", "w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=ordenamientos[0].keys()); w.writeheader(); w.writerows(ordenamientos)
    with open(RESULTADOS / "tiempos_busqueda.json", "w", encoding="utf-8") as f:
        json.dump(busquedas, f, ensure_ascii=False, indent=2)

    crear_graficos(ordenamientos, busquedas, str(RESULTADOS))
    print("CATÁLOGO: 50 productos")
    print("\nORDENAMIENTOS (promedio por ejecución, microsegundos)")
    for r in ordenamientos:
        print(f'{r["criterio"]:28} | {r["algoritmo"]:12} | {r["promedio_us"]:.3f} us')
    print("\nBÚSQUEDAS")
    for k,v in busquedas.items():
        print(f"{k}: {v}")
    print(f"\nArchivos generados en: {RESULTADOS}")

if __name__ == "__main__":
    main()
