#Escribe un programa que lea una cadena y devuelva un diccionario con la 
#cantidad de apariciones de cada carácter en la cadena. 

cad="hola como estas"
dic=dict.fromkeys(cad,0)
print(dic)
for i in cad:
    dic[i]+=1

print(dic)