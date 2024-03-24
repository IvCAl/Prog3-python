def agregarModificarContacto(agenda):
    nombre=input("Introduce el nombre del contacto: ")
    telefono=0
    if nombre in agenda:
        telefono=int(input("Introduce el teléfono a modificar. 0 para cancelar: "))
    else:
        telefono=int(input("Introduce un telefono nuevo, 0 para cancelar: "))
    if telefono!=0:
        agenda[nombre]=telefono
        return 0
    else:
        return -1   

def  eliminaContacto(agenda) :
    nombre = input ("Escribe el nombre del contacto que quieres eliminar: ")
    if not (nombre in agenda):
        print ("No existe ese contacto en tu agenda")
    else:
        b=input(f"Desea eliminar el contacto {nombre}?  s/n").lower()
        if b=="s":
            agenda.pop(nombre)
            print(f"\nSe ha eliminado el  contacto de la agenda.")
        elif b=="n":
            print("\nOperacion Cancelada.")
        else:
            print("\nComando no reconocido.")  

def muestraContacto(agenda,nombre):
    print(f'\nNombre: {nombre}')
    print(f"Telefono: {agenda[nombre]}")

def  buscaContactos(agenda):
    cad=input("\nIntroduzca un nombre para buscar: ").lower()
    b=0
    for i in agenda:
        if cad in i.lower():
            muestraContacto(agenda,i)
            b=1
    if b==0:
        print("No se encontraron coincidencias con su busqueda.")

def muestraAgenda(agenda):
    if len(agenda)==0:
        print("Agenda vacia. No hay contactos guardados.")
    else:
        for i in  agenda :
            muestraContacto(agenda,i)
def menu():
    op=-1
    while op<0 or op>4:
        op=int(input("1 - Agrega o modifica Contacto \n"
                     "2 - Buscar contactos \n"
                     "3 - Borrar un contacto\n"
                     "4 - Mostrar todos los contactos\n"
                     "0 - Para finalizar, Ingrese una opcion: "))
        if op<0 or op>4:
            print("Opcion incorrecta, ingrese nuevamente")
    return op

if  __name__ == '__main__':
    agenda=dict()
    op=menu()
    while op!=0:
        if  op==1:
            agregarModificarContacto(agenda)
        elif op==2:
            buscaContactos(agenda)
        elif op==3:
            eliminaContacto(agenda)
        elif op==4:
            muestraAgenda(agenda)

        op=menu()
    print("Adios")


