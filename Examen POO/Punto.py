class Punto:
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        else:
            self.x = x
            self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def mostrar(self):
        print("({},{})".format(self.x, self.y))

    def coordenadas(self):
        return "({},{})".format(self.x, self.y)
