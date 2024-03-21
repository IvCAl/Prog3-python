meses=["enero","febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
       "septiembre","octubre", "noviembre", "diciembre"]
diasxmes=[31,28,31,30,31,30,31,31,30,31,30,31]
mes=0
while mes<1 or mes>12:
    mes=int(input("Ingrese numero de mes: "))

print(f"El mes de {meses[mes-1]} tiene {diasxmes[mes-1]} dias.")