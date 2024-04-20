class persona:
    
    def __init__(self,nombre="",dni=0,edad=0):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
    
    def getEdad(self) :
        return self.edad
    def getNombre(self) :
        return self.nombre
    def setEdad(self,edad):
        self.edad=edad
    def setNombre(self,nombre):
        self.nombre=nombre
    def getDni(self):
        return self.dni
    def setDni(self,dni):
        self.dni=dni
       
x=persona()
x.setNombre("juan")