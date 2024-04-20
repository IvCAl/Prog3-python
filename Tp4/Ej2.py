from Ej1 import persona
class Cuenta:
    titular: persona
    __cantidad: float

    def __init__(self,titular:persona,cantidad=0.0):
        self.titular=titular
        self.__cantidad=cantidad
    
    def __str__(self) -> str:
        return f"Titular: \n{self.titular}\nCuenta: {self.getCantidad()}"

    def getCantidad(self):
        return self.__cantidad
    
    def ingresar(self,cantidad):
        if cantidad>0:
            self.__cantidad+=cantidad
    
    def retirar(self,cantidad):
        if cantidad>0:
            self.__cantidad-=cantidad
    def mostrar(self):
        print (self)