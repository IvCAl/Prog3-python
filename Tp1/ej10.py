def cargaProductos():
    arti=int(input("Ingrese cantidad de productos: "))
    lista=list()
    for art in range(arti):
        lista.append(input("Ingrese nombre del producto: "))
    return lista

def cargaSucursales():
    sucu=int(input("Ingrese cantidad de sucursales: "))
    lista=list()
    for suc in range(sucu):
        lista.append(input("Ingrese nombre de la sucursal: "))
    return lista

def cargaPrecios(productos):
    precios=list()
    for art in productos:
        precios.append(float(input(f"Ingrese precio de [{art}] : ")))
    return precios

def _cargaVentas(sucursales):
    lista=list()
    for suc in range(len(sucursales)):
        lista.append(int(input(f"Ingrese ventas en la sucursal [{sucursales[suc]}]: ")))
    return lista

def cargaVentasXSuc(productos,sucursales):
    ventas=list()
    for art in range(len(productos)):
        print(f"Para el producto {productos[art]}:")
        ventas.append(_cargaVentas(sucursales))
    return ventas

def ventasXArt(sucursales,ventasXsuc,prod):
    c=0
    for suc in range(len(sucursales)):
        c+=ventasXsuc[prod][suc]
    return c

def ventasXSuc(productos,ventasXsuc,suc):
    c=0
    for art in range(len(productos)):
        c+=ventasXsuc[art][suc]
    return c

def ventasXArtXSuc(ventasXsuc,art,suc):
    return ventasXsuc[art][suc]

def gananciaXSuc(precios,ventasXsuc,suc):
    c=0
    for art in range(len(precios)):
        c+=(precios[art]*ventasXsuc[art][suc])
    return c

#cantidades totales de cada articulo
def ej1(productos,sucursales,ventasXsuc):
    for art in range(len(productos)):
        print(f"Cantidad de [{productos[art]} : {ventasXArt(sucursales,ventasXsuc,art)}]")

#La cantidad de artículos en la sucursal 2.
def ej2(productos,sucursales,ventasXsuc):
    suc=2-1
    print(f"Ventas en la sucursal [{sucursales[suc]}]")
    for art in range(len(productos)):
        print(f"[{productos[art]}] : {ventasXArtXSuc(ventasXsuc,art,suc)}")

#La cantidad del articulo 3 en la sucursal 1
def ej3(productos,sucursales,ventasXsuc):
    art=3-1
    suc=1-1
    print(f"Ventas del producto [{productos[art]}] en la sucursal [{sucursales[suc]}] : "
          f"{ventasXArtXSuc(ventasXsuc,art,suc)}")

#La recaudación total de cada sucursal.
def ej4(precios,sucursales,ventasXsuc):
    for suc in range(len(sucursales)):
        print(f"Recaudacion total en la sucursal [{sucursales[suc]}] = ${gananciaXSuc(precios,ventasXsuc,suc)}")

#La recaudación total de la empresa.
def ej5(precios,sucursales,ventasXsuc):
    sum=0
    for suc in range(len(sucursales)):
        sum+=gananciaXSuc(precios,ventasXsuc,suc)
    print(f"La recaudacion total de la empresa es de ${sum}")
#La sucursal de mayor recaudación.
def ej6(precios,sucursales,ventasXsuc):
    may=0
    maysuc=0
    aux=0
    for suc in range(len(sucursales)):
        aux=gananciaXSuc(precios,ventasXsuc,suc)
        if aux>may:
            may=aux
            maysuc=suc
    print(f"Quien tiene mayor recaudacion es la sucursal [{sucursales[maysuc]}] con ${may}")


def menu():
    op=-1
    while op<0 or op>6:
        op=int(input("1 - Para ej1 \n"
                     "2 - para ej2 \n"
                     "3 - para ej3 \n"
                     "4 - para ej4 \n"
                     "5 - para ej5 \n"
                     "6 - para ej6 \n"
                     "0 - Para finalizar, Ingrese una opcion: "))
        if op<0 or op>6:
            print("Opcion incorrecta, ingrese nuevamente")
    return op

if __name__ == '__main__':
    sucursales=cargaSucursales()
    productos=cargaProductos()
    precios=cargaPrecios(productos)
    ventasXsuc=cargaVentasXSuc(productos,sucursales)

    op=menu()
    while(op!=0):
        if op==1:
            ej1(productos,sucursales,ventasXsuc)
        elif op==2:
            ej2(productos,sucursales,ventasXsuc)
        elif op==3:
            ej3(productos,sucursales,ventasXsuc)
        elif op==4:
            ej4(precios,sucursales,ventasXsuc)
        elif op==5:
            ej5(precios,sucursales,ventasXsuc)
        else:
            ej6(precios,sucursales,ventasXsuc)
            
        if op!=0:
            op=menu()
    print("Adios")