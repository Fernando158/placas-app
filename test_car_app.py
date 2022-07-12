import unittest
from main import *

class TestCarApp(unittest.TestCase):

    def test_get_patente_string(self):
        patente = 'AAAA000'

        id_patente = get_patente(patente)
        self.assertEqual(id_patente, {'patente_id': 1})
    
    def test_get_patente_int(self):
        patente = 1
        msg = 'La patente ingresada es incorrecta, verifique e intente nuevamente'

        with self.assertRaises(HTTPException) as exc:
            get_patente(patente)

        self.assertEqual(exc.exception.detail, msg)
    
    def test_get_patente_negativo(self):
        patente = -10
        msg = 'La patente ingresada es incorrecta, verifique e intente nuevamente'

        with self.assertRaises(HTTPException) as exc:
            get_patente(patente)

        self.assertEqual(exc.exception.detail, msg)

    def test_get_patente_bool(self):
        patente = True
        msg = 'La patente ingresada es incorrecta, verifique e intente nuevamente'

        with self.assertRaises(HTTPException) as exc:
            get_patente(patente)

        self.assertEqual(exc.exception.detail, msg)

    def test_get_patente_id_int(self):
        id_patente = 1

        patente = get_patente_id(id_patente)
        self.assertEqual(patente, {'patente': 'AAAA000'})
    
    def test_get_patente_id_string(self):
        id_patente = 'AAAA000'

        msg = 'La patente ingresada no existe, las patentes registradas estan en el rango del 1 al 26000'

        with self.assertRaises(HTTPException) as exc:
            get_patente_id(id_patente)

        self.assertEqual(exc.exception.detail, msg)
    
    def test_get_patente_id_superior(self):
        id_patente = 100000

        msg = 'La patente ingresada no existe, las patentes registradas estan en el rango del 1 al 26000'

        with self.assertRaises(HTTPException) as exc:
            get_patente_id(id_patente)

        self.assertEqual(exc.exception.detail, msg)
    
    def test_get_patente_id_negativo(self):
        id_patente = -10

        msg = 'La patente ingresada no existe, las patentes registradas estan en el rango del 1 al 26000'

        with self.assertRaises(HTTPException) as exc:
            get_patente_id(id_patente)

        self.assertEqual(exc.exception.detail, msg)