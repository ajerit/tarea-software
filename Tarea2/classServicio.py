from math import *
from datetime import *

class Servicio:

    def calcularPrecio(self, tarifa, tiempoDeServicio):
        if tiempoDeServicio[1] <= tiempoDeServicio[0]:
            return None
        
        tiempoDif=tiempoDeServicio[1]-tiempoDeServicio[0]
        diasDif=tiempoDif.days
        horasDif=ceil(tiempoDif.seconds/3600.0)
        
        if ((diasDif>7) or (tiempoDif.total_seconds()<60*15)): # Condiciones de borde
            return None
                
        if (diasDif==0): # Estadia de un solo dia
            if (tiempoDeServicio[0].weekday<5):
                if (horasDif!=0):
                    precio=horasDif*tarifa.sem
                else:
                    precio=tarifa.sem
            else:
                if (horasDif!=0):
                    precio=horasDif*tarifa.finsem
                else:
                    precio=tarifa.finsem
        else:
            diasSem=0
            diasFin=0
            
            unDia = timedelta(days=1)
            fechaActual = tiempoDeServicio[0]
            fechaTope = datetime(tiempoDeServicio[1].year, tiempoDeServicio[1].month, tiempoDeServicio[1].day)
            while (fechaActual < fechaTope): # Calcula el numero de dias de la semana y del fin
                if (fechaActual.weekday()<5):
                    diasSem=diasSem+1
                else:
                    diasFin=diasFin+1
                fechaActual += unDia
            
            if (diasSem == 1 and diasFin == 0):
                precio = 24 * tarifa.get_tsem() * horasDif
                return precio
            elif (diasSem == 0 and diasFin == 1):
                precio = 24 * tarifa.get_tfsem() * horasDif
                return precio
                
            # Calculo de las horas del primer dia
            if (tiempoDeServicio[0].weekday()<5): # Si es en la semana
                precio=(24-tiempoDeServicio[0].hour)*tarifa.sem
                diasSem=diasSem-1
            else: # Si es en fin de semana
                precio=(24-tiempoDeServicio[0].hour)*tarifa.finsem
                diasFin=diasFin-1
                
            # Calculo del ultimo dia de la semana
            if (tiempoDeServicio[1].weekday()<5): # Si es en la semana
                precio=precio+(tiempoDeServicio[1].hour * tarifa.sem)
                if tiempoDeServicio[1].minute > 0:
                    precio = precio + tarifa.sem
                diasSem=diasSem-1
            else: # Si es el fin de semana
                precio=precio+(tiempoDeServicio[1].hour * tarifa.finsem)
                if tiempoDeServicio[1].minute > 0:
                    precio = precio + tarifa.finsem
                diasFin=diasFin-1
                
            precio =precio+(24*diasSem*tarifa.sem)+(24*diasFin*tarifa.finsem) # Resto de las horas
        return precio