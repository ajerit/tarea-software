class Servicio:
    
    def calcularPrecio(self, tarifa, tiempoDeServicio):
        tiempoDif=tiempoDeServicio[1]-tiempoDeServicio[0]
        diasDif=tiempoDif.days
        if ((diasDif>7) or (tiempoDif.total_seconds()<60*15)): # Condiciones de borde
            return None
        
        if (tiempoDif==0): # Estadia de un solo dia
            if (tiempoDeServicio[0].weekday<5):
                precio=tiempoDif.hour*tarifa.sem
            else:
                precio=tiempoDif.hour*tarifa.finsem
        else:
            diasSem=0
            diasFin=0
            diasDif
            while (diasDif>0): # Calcula el numero de dias de la semana y del fin
                if (tiempoDeServicio[0].weekday()<5):
                    diasSem=diasSem+1
                else:
                    diasFin=diasFin+1
                diasDif=diasDif-1
            # Calculo de las horas del primer dia
            if (tiempoDeServicio[0].weekday()<5): # Si es en la semana
                precio=(23-tiempoDeServicio[0].hour)*tarifa.sem
                diasSem=diasSem-1
            else: # Si es en fin de semana
                precio=(23-tiempoDeServicio[0].hour)*tarifa.finsem
                diasFin=diasFin-1
            # Calculo del ultimo dia de la semana
            if (tiempoDeServicio[1].weekday()<5): # Si es en la semana
                precio=precio+(tiempoDeServicio[1].hour*tarifa.sem)
                diasSem=diasSem-1
            else: # Si es el fin de semana
                precio=precio+(tiempoDeServicio[1].hour*tarifa.finsem)
                diasFin=diasFin-1
            precio=precio+(24*diasSem*tarifa.sem)+(24*diasFin*tarifa.finsem) # Resto de las horas
        return precio