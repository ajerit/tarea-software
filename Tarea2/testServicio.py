import unittest
from datetime import *

from classServicio import Servicio
from classTarifa import Tarifa

class ClaseTarifaTest(unittest.TestCase):
    def setUp(self):
        self.t = Tarifa()
        
    def testTarifaInicialSem(self):
        self.assertEqual(self.t.get_tsem(), None)

    def testTarifaInicialFin(self):
        self.assertEquals(self.t.get_tfsem(), None)
    
    def testTarifaSetSem(self):
        self.t.set_tsem(50.5)
        self.assertEqual(self.t.get_tsem(), 50.5)
    
    def testTarifaSetFSem(self):
        self.t.set_tfsem(60.5)
        self.assertEqual(self.t.get_tfsem(), 60.5)
        
class ClaseServicioTest(unittest.TestCase):
    def setUp(self):
        self.s = Servicio()
        self.t = Tarifa()
    
    def tearDown(self):
        self.s = None
        self.t = None
    
    # Caso frontera minima de Tarifa
    def testTarifaCero(self):
        self.t.set_tsem(0)
        self.t.set_tfsem(0)
        servicio = [datetime(2017, 1, 1), datetime(2017, 1, 2)]
        self.assertEquals(self.s.calcularPrecio(self.t, servicio), 0)
       
    # Caso frontera minima de tiempo
    def testTiempoMenos15Min(self):
        servicio = [datetime(2017, 1, 1, 7, 0), datetime(2017, 1, 1, 7, 14)]
        self.assertEquals(self.s.calcularPrecio(self.t, servicio), None)
        
    # Caso frontera maxima de tiempo    
    def testTiempoMayor7Dias(self):
        servicio = [datetime(2017, 1, 1), datetime(2017, 1, 9)]
        self.assertEquals(self.s.calcularPrecio(self.t, servicio), None)

if __name__ == "__main__":
    unittest.main()