class Punto:
    def __init__(self, x=None, y=None):
        if x==None and y == None:
            self.x=0
            self.y=0
        else:
            self.x = x
            self.y = y

    def mostrar(self):
        print("({},{})".format(self.x, self.y))

    def coordenadas(self):
        return "({},{})".format(self.x,self.y)
