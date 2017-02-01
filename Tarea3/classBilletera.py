#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classRecarga import Recarga
from classConsumo import Consumo
from __builtin__ import False

class Billetera:
    
    def __init__(self, id_b, n, a, ci, pin):
        self.id = id_b
        self.nombre = n + " " + a
        self.ci = ci
        self.pin = pin
        self.registro_consumo = []
        self.registro_recargas = []
        self.saldo = 0
        
    def get_saldo(self):
        return self.saldo
    
    def recargar(self, m, f, id_est):
        if m < 0:
            return False
        
        r = Recarga(m, f, id_est)
        self.registro_recargas.append(r)
        self.saldo=self.saldo+m
        
    def consumir(self, pin, m, f, id_est):
        if pin != self.pin:
            return False
        else:
            if self.saldo < m:
                return False
            else:
                c = Consumo(m, f, id_est)
                self.registro_consumo.append(c)
                self.saldo = self.saldo - m
                return True
                
            
        
        
        