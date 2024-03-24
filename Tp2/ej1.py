#1- Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas 
#claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

n=int(input("ingrese un numero: "))
dic=dict()
for i in range(1,n+1,1):
    dic[i]=i*i

print(dic)