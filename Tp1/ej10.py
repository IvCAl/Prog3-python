def cargaProductos():
    cant=int(input("Ingrese cantidad de productos: "))
    lista=list()
    for i in range(cant):
        lista.append(input("Ingrese nombre del producto: "))
    return cant

def

if __name__ == '__main__':
    
    productos=cargaProductos()
    precios=cargaPrecios(productos)
    nombre=cargaConductores()
    kms=cargaMatriz(nombre)
    horasTotalesXConductor=sumaFilas(kms,nombre,dias)
    
    for i in range(len(nombre)):
        print(f"{nombre[i]} condujo {horasTotalesXConductor[i]} horas.")