from Ej7 import Punto

class Rectangulo:
    p1:Punto
    p2:Punto

    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.p1=Punto(x1,y1)
        self.p2=Punto(x2,y2)

    def base(self):
        return abs(self.p2.getX()-self.p1.getX())
    def altura(self):
        return abs(self.p2.getY()-self.p1.getY())
    def area(self):
        return self.base()*self.altura()