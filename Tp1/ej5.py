import random
lista=list()

for i in range(10):
    lista.append(random.randint(0,100))

lista.sort()
print(lista)