import unittest

from classServicio import Servicio
from classTarifa import Tarifa

class ClaseTarifaTest(unittest.TestCase):
    def setUp(self):
        self.t = Tarifa()
        
    def testTarifaInicialSem(self):
        self.assertEqual(self.t.get_tsem(), None, "Tarifa Semanal se inicializo")

    def testTarifaInicialFin(self):
        self.assertEquals(self.t.get_tfsem(), None, "Tarifa Fin de Semana se inicializo")
    
    def testTarifaSetSem(self):
        self.assertEqual(self.t.get_tsem(), 50.5)
        
class ClaseServicioTest(unittest.TestCase):
    def setUp(self):
        self.s = Servicio()
    

if __name__ == "__main__":
    unittest.main()