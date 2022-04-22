class ROP:
    def __init__(self,demanda,dias_laborales,plazo_entrega):
        self.demanda = demanda
        self.dias_laborales = dias_laborales
        self.plazo_entrega = plazo_entrega
        

    def calcular_rop(self):
        demanda_por_dia = float(self.demanda / 360)
        rop = float(demanda_por_dia*self.plazo_entrega)
        return rop 


#prueba xd

rop_p = ROP(1500000,360,2)
ROP=rop_p.calcular_rop()
