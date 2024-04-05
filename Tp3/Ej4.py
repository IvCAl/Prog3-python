def sumaElementos(arr:list) -> float:
    try:
        suma:float=0.0
        for i in arr:
            suma+=i
        return suma
    except TypeError:
        print("Los elementos deben ser numeros.")

def multiplicaElementos(arr:list) -> float:
    try:
        producto:float = 1.0
        for i in arr:
            producto *= i
        return producto
    except TypeError:
        print("Los elementos deben ser numeros.")

print(multiplicaElementos([1,2,"2",4]))
print(sumaElementos([1,2,3,4]))