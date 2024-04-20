import itertools

class sublistas:
    def __init__(self):
        self.sublista=[]
        
    def obtenerSublistas(self,lista:list):
        self.sublista=[]
        n=len(lista)
        for i in range(1,n+1):
            self.sublista.extend(set(itertools.combinations(lista,i)))
        return self.sublista


a=sublistas()
print(a.obtenerSublistas([1,2,3]))
