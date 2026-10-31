"""Pruebas automatizadas: ejecutar con python -m unittest -v."""
import unittest
from utilidades import (
    registrar_libro, buscar_libro, registrar_socio, analizar_prestamos
)

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.catalogo = {"L001": {"titulo": "Libro A", "autor": "Autora A"}}
        self.socios = {"S001"}

    def test_registrar_libro(self):
        self.assertTrue(registrar_libro(self.catalogo, "L002", "Libro B", "Autor B"))
        self.assertIn("L002", self.catalogo)

    def test_no_permite_codigo_duplicado(self):
        with self.assertRaises(ValueError):
            registrar_libro(self.catalogo, "L001", "Otro", "Autor")

    def test_buscar_libro_existente(self):
        self.assertEqual(buscar_libro(self.catalogo, "L001")["titulo"], "Libro A")

    def test_buscar_libro_inexistente(self):
        self.assertIsNone(buscar_libro(self.catalogo, "L999"))

    def test_registrar_socio_y_evitar_duplicado(self):
        self.assertTrue(registrar_socio(self.socios, "S002"))
        self.assertFalse(registrar_socio(self.socios, "S001"))
        self.assertEqual(len(self.socios), 2)

    def test_operaciones_conjuntos(self):
        resultado = analizar_prestamos({"S1", "S2"}, {"S2", "S3"})
        self.assertEqual(resultado["ambos"], {"S2"})
        self.assertEqual(resultado["solo_novela"], {"S1"})
        self.assertEqual(resultado["total"], {"S1", "S2", "S3"})

if __name__ == "__main__":
    unittest.main()
