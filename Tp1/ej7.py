
lista1=list()
lista2=list()
lista3=list()

for i in range(2):
    lista1.append(int(input("ingrese un valor entero: ")))
    lista2.append(int(input("ingrese un valor entero: ")))
    lista3.append(lista1[i]+lista2[i])

print(lista3)