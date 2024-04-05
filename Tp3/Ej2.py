def CalcularFactorial(n:int):
    try:
        if n<0:
            print("No se puede calcular factorial negativo")
        elif n==0 or n==1:
            return 1
        else:
            return n*CalcularFactorial(n-1)
    except TypeError:
        print("Error, el valor debe ser numerico")

print(CalcularFactorial("1"))
print(CalcularFactorial(-1))
print(CalcularFactorial(0))
print(CalcularFactorial(1))
print(CalcularFactorial(2))