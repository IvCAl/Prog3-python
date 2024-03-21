import random

lista= list()
for i in  range(10):
    lista.append(random.randint(1,10))
    print(f"Elemento [{i+1}] = {lista[i]}\n"
          f"Cuadrado = {lista[i]**2}\n"
          f"Cubo = {lista[i]**3}\n")