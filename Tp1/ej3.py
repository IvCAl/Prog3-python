diccionario=dict()
materias=["Lengua","matematicas","historia","arte", "fisica"]
men=10
menMat=""
may=0
mayMat=""
suma=0
for i in materias:
    nota=int(input(f"Ingrese nota de {i}: "))
    suma+=nota
    diccionario[i]=nota
    if nota<men:
        men=nota
        menMat=i
    if nota>may:
        may=nota
        mayMat=i


print(f"Notas: {diccionario}\n"
      f"Promedio: {suma/len(materias)}\n"
      f"Mejor materia: {mayMat} con nota: {may}\n"
      f"Peor materia: {menMat} con nota: {men}\n")
