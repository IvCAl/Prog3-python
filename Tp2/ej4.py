#Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase
#y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
#Guarda la información en un diccionario cuya claves serán los nombres de los alumnos 
#y los valores serán listas con las notas de cada alumno.
def cargaAlumno(alumnos):
    nombre = input("Introduce el nombre del alumno: ")
    if nombre not in  alumnos:
        alumnos[nombre]=list()
        nota=0
        while nota!=-1:
            nota = int(input("Introduce la nota, -1  para terminar: "))
            if nota !=-1 :
                alumnos[nombre].append(nota)
        return 0
    else:
        print("El alumno ya existe")
        return -1

def cargaAlumnos(alumnos):
    n=int(input("Ingrese cantidad de alumnos: "))
    for i in range(n):
        r=cargaAlumno(alumnos)
        while r==-1:
            r=cargaAlumno(alumnos)

def calculaPromedios(alumnos):
    sumanotas=0
    for i in alumnos:
        print(alumnos[i])
        sumanotas=int(sum(alumnos[i]))
        promedio=sumanotas/len(alumnos[i])
        print ("El promedio de ",i,"es :",promedio)

if __name__ == '__main__':
    alumnos=dict( )
    cargaAlumnos(alumnos)
    calculaPromedios(alumnos)
