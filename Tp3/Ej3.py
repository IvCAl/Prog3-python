def convertirASegundos(horas:int,minutos:int,segundos:int):
    try:
        return horas*3600 + minutos*60  + segundos
    except TypeError:
        print("Error en los tipos de datos")

def convertirAHMS(segundos:int):
    try:
        horas=int(segundos/3600)
        segundos=segundos%3600
        min=int(segundos/60)
        segundos=segundos%60
        return f"{horas} hs {min} min {segundos} seg"
    except TypeError:
        print("Error en el tipo de dato")

def menu():
    op=-1
    while op<0 or op>2:
        op=int(input("1 - Convertir a segundos \n"
                     "2 - Convertir a HH:MM:SS \n"
                     "0 - Para finalizar, Ingrese una opcion: "))
        if op<0 or op>2:
            print("Opcion incorrecta, ingrese nuevamente")
    return op

if  __name__ == '__main__':
    h=m=s=0
    op=menu()
    while op!=0:
        if  op==1:
            s=int(input("Ingrese los segundos: "))
            m=int(input("Ingrese los minutos: "))
            h=int(input("Ingrese las horas: "))
            print(f"[+{h} hs {m} min {s} seg equivalen a {convertirASegundos(h,m,s)} segundos")
        elif op==2:
            s=int(input("Ingrese los segundos: "))
            print(f"{s} segundos equivalen a {convertirAHMS(s)}")
        op=menu()
    print("Adios")