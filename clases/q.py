from math import sqrt


class q:
    def __init__(self,demanda,costo_pedir,costo_almacen,costo_compra):
        self.demanda = demanda
        self.costo_pedir = costo_pedir
        self.costo_almacen = costo_almacen
        self.costo_compra = costo_compra

    def calcular_q(self):
        costo_almacen_decimal = float(self.costo_almacen / 100)
        q = sqrt((2*float(self.demanda) * float(self.costo_pedir)) / (float(costo_almacen_decimal) * float(self.costo_compra)))
        return q


#Prueba
william = q(1500000,80,10,2.5)
print(william.calcular_q())