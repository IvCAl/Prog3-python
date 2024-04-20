
class lista:
    def __init__(self):
        pass
    
    def buscarEnLista(self,lista:list,num:int):
        n=len(lista)
        x=-1
        y=-1
        for i in range(n-1):
            for j in range(i+1,n):
                if lista[i]+lista[j]==num:
                    x=i
                    y=j
                    break
        if x!=-1 and y!=-1:
            return [x,y]
        else:
            return "No se encontro combinacion"

a=lista()
print(a.buscarEnLista([1,2,3],6))