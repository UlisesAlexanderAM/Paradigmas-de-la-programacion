from Punto import Punto

class Rectangulo:
    def __init__(self, **kwargs):
        self.punto_a = kwargs["punto_a"]
        self.punto_b = kwargs["punto_b"]
        self.punto_c = kwargs["punto_c"]
        self.punto_d = kwargs["punto_d"]
        self.base = kwargs["base"]
        self.altura = kwargs["altura"]

    def calcularBase(self):
        pass
