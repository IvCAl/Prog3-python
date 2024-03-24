#Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar 
#los precios de las distintas frutas. El programa pedirá el nombre de la fruta 
#y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir 
#de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
#Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

def menu():
    op=-1
    while op<0 or op>3:
        op=int(input("1 - Cargar una fruta \n"
                     "2 - Consultar fruta \n"
                     "3 - Consultar ganancias\n"
                     "0 - Para finalizar, Ingrese una opcion: "))
        if op<0 or op>3:
            print("Opcion incorrecta, ingrese nuevamente")
    return op

def cargaFruta(frutas):
    fruta=(input("Ingrese fruta: ")).lower()
    if fruta not in frutas:
        cant=int(input("Ingrese cantidad vendida: "))
        precio=float(input("Ingrese precio: "))
        frutas[fruta]=[cant,precio]
    else:
        print("La fruta ya existe")
        
def consultarFruta(frutas):
    fruta=(input("Ingrese fruta: ")).lower()
    if fruta in frutas:
        print(f"[{fruta}] cuesta: ${frutas.get(fruta)[1]}")
    else:
        print("La fruta indicada no se encuentra en la lista")

def verGananciasXFruta(frutas):
    for i in frutas:
        print(f"Con [{i}] se vendio [{frutas.get(i)[0]}] y se obtuvo ${frutas.get(i)[0]*frutas.get(i)[1]}")

if __name__ == '__main__':
    frutas=dict()
    
    op=menu()
    while(op!=0):
        if op==1:
            cargaFruta(frutas)
        elif op==2:
            consultarFruta(frutas)
        else:
            verGananciasXFruta(frutas)
            
        op=menu()
    print("Adios")