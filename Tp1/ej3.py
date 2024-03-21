notas=list()
materias=["Lengua","matematicas","historia","arte", "fisica"]
men=0
menMat=""
may=0
mayMat=""
suma=0
for i in range(len(materias)):
    nota=int(input(f"Ingrese nota de {materias[i]}: "))
    suma+=nota
    notas.append(nota)
    if nota<notas[men]:
        men=i
    if nota>notas[may]:
        may=i

for i in range(5):
    print(f"{materias[i]}: {notas[i]}")
print(f"Promedio: {suma/len(materias)}\n"
      f"Mejor materia: {materias[may]} con nota: {notas[may]}\n"
      f"Peor materia: {materias[men]} con nota: {notas[men]}\n")
