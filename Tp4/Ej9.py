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
    def suma(a:Entero, b:Entero):
        return Entero(a.getNumero + b.getNumero)
    def resta(a:Entero,b:Entero):
        return Entero(a.getNumero - b.getNumero)
    def producto(a:Entero,b:Entero):
        return Entero(a.getNumero * b.getNumero)
    def division(a:Entero,b:Entero):
        if b.getNumero == 0:
            print("No se puede dividir por 0")
            return Entero()
        else:
            return Entero(a.getNumero / b.getNumero)
    