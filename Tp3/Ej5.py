def elevaElementos(arr:list, n:int):
    try:
        aux=list()
        for i in arr:
            aux.append(i**n)
        return aux
    except TypeError:
        print("Todos los elementos deben ser numericos")


print(elevaElementos([2,3,4],2))