class persona:
    nombre:str
    edad:int
    dni:int
    def __init__(self,nombre='',edad=0,dni=0):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}"
    
    
    def isAdult(self) -> bool:
        if self.edad>=18:
            return True
        else:
            return False
        
x=persona()

print(x)