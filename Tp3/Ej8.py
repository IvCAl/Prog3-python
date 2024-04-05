import random
import string

def generarClaves(arr:list,cantidad:int,longitud:int):
    try:
        for  i in range(cantidad):
            cad:str = ""
            for j in range(longitud):
                cad=f"{cad}{random.choice(string.ascii_letters + string.digits)}"
            arr.append(cad)
    except TypeError:
        print("Error en los parametros")

claves=list()

generarClaves(claves,3,12)

print(claves)