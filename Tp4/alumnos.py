from persona import persona

class alumnos (persona):
    nota: int
    
    def __init__(self, nombre, dni, edad, nota):
        super().__init__(nombre, dni, edad)
        self.nota=nota

    def verRegularidad(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("No regular")