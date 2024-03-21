def cargaMatriz(filas:int,columnas:int):
    matriz=list()
    for i in range (filas):
        fila=list()
        for j in range(columnas):
            fila.append(int(input("Ingrese un numero entero: ")))
        matriz.append(fila)
    return matriz

def _sumaFila(matriz,fila:int,columna:int):
    suma=0
    for i in range(columna):
        suma+=matriz[fila][i]
    return suma

def sumaFilas(matriz,fila:int,columna:int):
    lista=list()
    for i in range(fila):
        lista.append(_sumaFila(matriz,i,columna))
    return lista

def _sumaColumna(matriz,fila:int,columna:int):
    suma=0
    for i in range(fila):
        suma+=matriz[i][columna]
    return suma

def sumaColumnas(matriz,fila:int,columna:int):
    lista=list()
    for i in range(columna):
        lista.append(_sumaColumna(matriz,fila,i))
    return lista

def muestraMatriz(matriz,fila:int,columna:int):
    print(f"Matriz de {fila} x {columna} : ")
    for i in range(fila):
        print(matriz[i])
if __name__ == '__main__':
    fil=2
    col=2
    matriz=cargaMatriz(fil,col)
    arraySumaFila=sumaFilas(matriz,fil,col)
    arraySumaColumna=sumaColumnas(matriz,fil,col)
    muestraMatriz(matriz,fil,col)
    for i in range(fil):
        print(f"Suma de Fila [{i}] = {arraySumaFila[i]}")
    for i in range(col):
        print(f"Suma de Columna [{i}] = {arraySumaColumna[i]}")
