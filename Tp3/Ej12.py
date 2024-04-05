def cuentaMayusculas():
    cad=input("Ingrese una frase: ")
    count=0
    for i in cad:
        if (i==i.upper()) and (i!=" "):
            count+=1
    print(f"El texto tiene {count} letras mayusculas")


cuentaMayusculas()