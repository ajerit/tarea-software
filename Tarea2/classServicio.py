import datetime
from classTarifa import Tarifa

class Servicio:

    def calcularPrecio(self, tarifa, tiempoDeServicio):
        tiempoDif = tiempoDeServicio[1] - tiempoDeServicio[0]
        diasDif = tiempoDif.days
        if (tiempoDif == 0):
            if (tiempoDeServicio[0].weekday < 5):
                precio = tiempoDif.hours*tarifa.sem
            else:
                precio = tiempoDif.hours*tarifa.finsem
        else:
            diasSem = 0
            diasFin = 0
            i = diasDif
            while (i > 0):
                if (tiempoDeServicio[0].weekday() < 5):
                    diasSem += 1
                else:
                    diasFin += 1
                i -= 1
            if (tiempoDeServicio[0].weekday() < 5):
                precio= (23 - tiempoDeServicio.hours)*tarifa.sem
                diasSem -= 1
            else:
                precio=(23 - tiempoDeServicio.hours)*tarifa.finsem
                diasFin -= 1
            if (tiempoDeServicio[1].weekday() < 5):
                precio= precio + (tiempoDeServicio[1]*tarifa.sem)
                diasSem -= 1
            else:
                precio = precio + (tiempoDeServicio[1]*tarifa.finsem)
                diasFin -= 1
            precio = precio + (diasSem*tarifa.sem) + (diasFin*tarifa.fin)
        return precio