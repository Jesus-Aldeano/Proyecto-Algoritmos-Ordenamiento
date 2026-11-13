import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import unittest
from generador import generar_productos
from ordenamientos import merge_sort, quick_sort, heap_sort
from busquedas import busqueda_binaria_por_id, busqueda_lineal_por_subcadena

class TestProyecto(unittest.TestCase):
    def setUp(self):
        self.productos = generar_productos(50, 2026)

    def test_cantidad_e_ids_unicos(self):
        self.assertEqual(len(self.productos), 50)
        ids = [p.id for p in self.productos]
        self.assertEqual(len(ids), len(set(ids)))

    def test_algoritmos_precio(self):
        for algoritmo in (merge_sort, quick_sort, heap_sort):
            ordenados = algoritmo(self.productos, lambda p: p.precio)
            self.assertEqual([p.precio for p in ordenados],
                             sorted(p.precio for p in self.productos))

    def test_algoritmos_calificacion_descendente(self):
        for algoritmo in (merge_sort, quick_sort, heap_sort):
            ordenados = algoritmo(self.productos, lambda p: -p.calificacionPromedio)
            valores = [p.calificacionPromedio for p in ordenados]
            self.assertEqual(valores, sorted(valores, reverse=True))

    def test_busqueda_binaria(self):
        ordenados = sorted(self.productos, key=lambda p: p.id)
        for p in self.productos:
            self.assertEqual(busqueda_binaria_por_id(ordenados, p.id).id, p.id)
        self.assertIsNone(busqueda_binaria_por_id(ordenados, 999))

    def test_busqueda_subcadena(self):
        resultados = busqueda_lineal_por_subcadena(self.productos, self.productos[0].nombre.split()[0])
        self.assertTrue(resultados)
        self.assertEqual(busqueda_lineal_por_subcadena(self.productos, "no_existe_xyz"), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)
