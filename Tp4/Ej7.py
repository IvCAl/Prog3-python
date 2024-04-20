from __future__ import annotations
class Punto:
    xy:list

    def __init__(self,x=0,y=0):
        self.xy=[x,y]
    def __str__(self):
        return f"({self.xy[0]},{self.xy[1]})"
    def getX(self):
        return self.xy[0]
    def getY(self):
        return self.xy[1]
    def getCuadrante(self):
        x=self.getX
        y=self.getY
        s:str
        if(x==0):
            if(y==0):
                s="El punto se encuentra en el Origen"
            else:
                s="El punto se encuentra en el eje Y"
        elif(y==0):
            s="El punto se encuentra en el eje X"
        elif(x>0 and y>0):
            s="El punto se encuentra en el primer cuadrante"
        elif(x<0 and y>0):
            s="El punto se encuentra en el segundo cuadrante"
        elif(x<0 and y<0):
            s="El punto se encuentra en el tercer cuadrante"
        else:
            s="El punto se encuentra en el cuarto cuadrante"
        return s
    
    def vector(self,Q:Punto):
        x1=self.getX
        y1=self.getY
        x2=Q.getX
        y2=Q.getY
        return Punto(x2-x1,y2-y1)
