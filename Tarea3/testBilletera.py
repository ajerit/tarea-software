#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classBilletera import Billetera
import unittest
import datetime

class TestBilletera(unittest.TestCase):
        #Tests para el metodo obtener saldo
    def test_Borde_Inicio_S(self):
        BilleteraP = Billetera("id15","juan","perez","24506213",111)
        self.assertEqual(0,BilleteraP.get_saldo())      

    #Tests para el metodo de recarga
    def test_Borde_Inicio_R(self):
        BilleteraP = Billetera("id15","juan","perez","24506213",111)
        monto = 10
        fecha = datetime.datetime(2017, 1, 23,3,0)
        id = 1
        BilleteraP.recargar(monto,fecha , id)
        self.assertEqual(monto,BilleteraP.registro_recargas[0].monto)
        self.assertEqual(fecha,BilleteraP.registro_recargas[0].fecha)
        self.assertEqual(id,BilleteraP.registro_recargas[0].id)
    
    def test_Borde_Transaccion_R(self):
        BilleteraP = Billetera("id15","juan","perez","24506213",111)
        monto = 10
        fecha = datetime.datetime(2017, 1, 23,3,0)
        id = 1
        BilleteraP.recargar(monto,fecha , id)
        self.assertEqual(monto,BilleteraP.registro_recargas[0].monto)
        self.assertEqual(fecha,BilleteraP.registro_recargas[0].fecha)
        self.assertEqual(id,BilleteraP.registro_recargas[0].id)
        self.assertEqual(10,BilleteraP.get_saldo())    
    #Tests para el metodo de consumo
    def test_Borde_Consumo_c(self):
        BilleteraP = Billetera("id15","juan","perez","24506213",111)
        pin=111
        monto = 10
        fecha = datetime.datetime(2017, 1, 23,3,0)
        id = 1
        BilleteraP.recargar(monto,fecha , id)
        BilleteraP.consumir(pin,monto,fecha , id)
        self.assertEqual(monto,BilleteraP.registro_consumo[0].monto)
        self.assertEqual(fecha,BilleteraP.registro_consumo[0].fecha)
        self.assertEqual(id,BilleteraP.registro_consumo[0].id)
        self.assertEqual(0,BilleteraP.get_saldo())    
    #Test maliciosos
    def test_Borde_Nombre(self):
        BilleteraP = Billetera("id15","Píngúñó","Perez","24506213",111)
        self.assertEqual("Píngúñó Perez",BilleteraP.nombre)  
    def test_Borde_Consumo_Mas(self):
        BilleteraP = Billetera("id15","juan","perez","24506213",111)
        pin=111
        monto = 10
        fecha = datetime.datetime(2017, 1, 23,3,0)
        id = 1
        BilleteraP.recargar(monto,fecha , id)
        BilleteraP.consumir(pin,monto+1,fecha , id)
        self.assertEqual(10,BilleteraP.get_saldo())   
    def test_pin_falso(self):
        BilleteraP = Billetera("id15","juan","perez","24506213",111)
        pin=111
        monto = 10
        fecha = datetime.datetime(2017, 1, 23,3,0)
        id = 1
        BilleteraP.recargar(monto,fecha , id)
        BilleteraP.consumir(114,monto,fecha , id)
        self.assertEqual(10,BilleteraP.get_saldo())  
    def test_recarga_negativa(self):
        BilleteraP = Billetera("id15","juan","perez","24506213",111)
        pin=111
        monto = -10
        fecha = datetime.datetime(2017, 1, 23,3,0)
        id = 1
        BilleteraP.recargar(monto,fecha , id)
        self.assertEqual(0,BilleteraP.get_saldo())  
    def test_Consumo_negativa(self):
        BilleteraP = Billetera("id15","juan","perez","24506213",111)
        pin=111
        monto = -10
        fecha = datetime.datetime(2017, 1, 23,3,0)
        id = 1
        BilleteraP.consumir(111,monto,fecha , id)
        self.assertEqual(0,BilleteraP.get_saldo())  