dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

def cargaMatriz(conductores):
    matriz=list()
    for i in range (len(conductores)):
        fila=list()
        print(f"Ingrese las horas que condujo {conductores[i]}:")
        for j in range(len(dias)):
            fila.append(int(input(f"El dia {dias[j]}: ")))
        matriz.append(fila)
    return matriz

def _sumaFila(matriz,fila,dias):
    suma=0
    for i in range(len(dias)):
        suma+=matriz[fila][i]
    return suma

def sumaFilas(matriz,conductores,dias):
    lista=list()
    for i in range(len(conductores)):
        lista.append(_sumaFila(matriz,i,dias))
    return lista

def cargaConductores():
    lista=list()
    i=int(input("Cuantos conductores quiere cargar?: "))
    while i>0:
        i-=1
        lista.append(input("Ingrese nombre del conductor: "))

    return lista

if __name__ == '__main__':
    
    nombre=cargaConductores()
    kms=cargaMatriz(nombre)
    horasTotalesXConductor=sumaFilas(kms,nombre,dias)
    
    for i in range(len(nombre)):
        print(f"{nombre[i]} condujo {horasTotalesXConductor[i]} horas.")