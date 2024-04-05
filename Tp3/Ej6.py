def decToBin(n:int):
    try:
        if n>1:
            return f"{decToBin(n//2)}{n%2}"
        else:
            return f"{n}"
    except TypeError:
        print("Solo se admiten numeros enteros")
def otroDecToBin(n:int):
    try:
        return f"{n:b}"
    except TypeError:
        print("Solo se admiten numeros enteros")

def binToDec(n:int):
    try:
        d=0
        for i in str(n):
            d=d*2+int(i)
        return d
    except TypeError:
        print("Solo se admiten numeros  en base 2")

print(decToBin(10))
print(otroDecToBin(10))
print(binToDec(1010))