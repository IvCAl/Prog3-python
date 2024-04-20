from Ej1 import persona
class Alumno(persona):
    lengua:int
    matematicas:int
    historia:int
    geografia:int
    comision:{'A','B','C','N'}
    def __init__(self, nombre='', edad=0, dni=0,lengua=0,matematicas=0,historia=0,geografia=0):
        super().__init__(nombre, edad, dni)
        self.lengua=lengua
        self.matematicas=matematicas
        self.historia=historia
        self.geografia=geografia
        prom=(lengua+matematicas+historia+geografia)/4
        if self.isAdult():
            self.comision='N'
        elif prom >=8:
            self.comision='A'
        elif prom >=6:
            self.comision='B'
        else:
            self.comision='C'
    
    def setNotaLengua(self,nota):
        self.lengua=nota
    def setNotaMatematicas(self,nota):
        self.matematicas=nota
    def setNotaHistoria(self,nota):
        self.historia=nota
    def setNotaGeografia(self,nota):
        self.geografia=nota


class Profesor(persona):
    materia:{'lengua','matematicas','historia','geografia'}
    def __init__(self, nombre='', edad=0, dni=0,materia=''):
        super().__init__(nombre, edad, dni)
        self.materia=materia
    def calificaAlumno(self,alumno:Alumno,nota=1):
        if self.materia=='lengua':
            alumno.setNotaLengua(nota)
        elif self.materia=='matematicas':
            alumno.setNotaMatematicas(nota)
        elif self.materia=='historia':
            alumno.setNotaHistoria(nota)
        elif self.materia=='geografia':
            alumno.setNotaGeografia(nota)