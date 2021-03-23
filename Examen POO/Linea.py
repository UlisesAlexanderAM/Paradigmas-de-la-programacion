from Punto import Punto


class Linea:

    def __init__(self, punto_a=Punto(), punto_b=Punto()):
        if punto_a is None and punto_b is None:
            self.punto_a = Punto(0, 0)
            self.punto_b = Punto(0, 0)
        else:
            self.punto_a = punto_a
            self.punto_b = punto_b

    def mueveDerecha(self, des):
        setattr(self.punto_a, 'x', self.punto_a.x + des)
        setattr(self.punto_b, 'x', self.punto_b.x + des)

    def mueveIzquierda(self, des):
        setattr(self.punto_a, 'x', self.punto_a.x - des)
        setattr(self.punto_b, 'x', self.punto_b.x - des)

    def mueveArriba(self, des):
        setattr(self.punto_a, 'y', self.punto_a.y + des)
        setattr(self.punto_b, 'y', self.punto_b.y + des)

    def mueveAbajo(self, des):
        setattr(self.punto_a, 'y', self.punto_a.y - des)
        setattr(self.punto_b, 'y', self.punto_b.y - des)

    def mostrarLinea(self):
        print("[{} , {}]".format(self.punto_a.coordenadas(), self.punto_b.coordenadas()))
