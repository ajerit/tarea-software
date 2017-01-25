class Tarifa: 
    def __init__(self, sem, finsem):
        self.sem = sem
        self.finsem = finsem
        
    def to_s(self):
        print("Tarifa semanal: %s \nTarifa fin de semana: %s" % self.sem, self.finsem)
        
    def get_tsem(self):
        return self.sem
    
    def set_tsem(self, new):
        self.sem = new
    
    def get_tfsem(self):
        return self.finsem
    
    def set_tfsem(self, new):
        self.finsem = new
    
    
    