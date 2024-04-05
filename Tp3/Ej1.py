def esMultiplo(a:int,b:int):
    try:
        if(a%b==0):
            return True
        else:
            return False
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except TypeError:
        print("Tipo de dato incorrecto")


print(esMultiplo(12,0))
print(esMultiplo(12,"2"))
print(esMultiplo(12,5))
print(esMultiplo(12,3))
