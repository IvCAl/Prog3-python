from __future__ import annotations
class Entero:
    numero:int
    def __init__(self, numero=0):
        self.numero = numero
    
    def __str__(self):
        return f"{self.numero}"
    def getNumero(self):
        return self.numero
    def setNumero(self, numero):
        self.numero = numero
    def __add__(a:Entero, b:Entero):
        return Entero(a.getNumero + b.getNumero)
    def __sub__(a:Entero,b:Entero):
        return Entero(a.getNumero - b.getNumero)
    def __mul__(a:Entero,b:Entero):
        return Entero(a.getNumero * b.getNumero)
    def __truediv__(a:Entero,b:Entero):
        if b.getNumero == 0:
            print("No se puede dividir por 0")
            return Entero()
        else:
            return Entero(a.getNumero / b.getNumero)
    