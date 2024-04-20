from Ej1 import persona
from Ej2 import Cuenta

class CuentasBancarias:
    cuentas:list

    def __init__(self):
        self.Cuentas = []

    def agregarCuenta(self, cuenta:Cuenta):
        self.Cuentas.append(cuenta)
    
    def muestraSaldoDeudor(self):
        cant=0.0
        for i in self.Cuentas:
            if i.getCantidad() < 0:
                cant-=i.getCantidad()
        print(f"Total adeudado: ${cant}")

    def muestraDeudores(self):
        print("Deudores:")
        for i in self.Cuentas:
            if i.getCantidad() < 0:
                print(i)


a= CuentasBancarias()
a.agregarCuenta(Cuenta(persona("pepe",0,0)))
a.agregarCuenta(Cuenta(persona("juan",0,0)))
a.agregarCuenta(Cuenta(persona("pedro",0,0),-2))
a.agregarCuenta(Cuenta(persona("joaquin",0,0),-1))

a.muestraDeudores()
a.muestraSaldoDeudor()