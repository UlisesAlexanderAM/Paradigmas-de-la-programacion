class Empleados:
    def __init__(self, salario, diasAsistidos):
        self.salario = salario
        self.diasAsistidos = diasAsistidos

    def calcularBonoAsistencia(self):
        if self.diasAsistidos == 30:
            self.salario *= 1.2
            cadena="El salario despues del bono es {}".format(self.salario)
        else:
            descuento = self.diasAsistidos * 100
            self.salario -= descuento
            cadena="El salario depues despues del descuento es {}".format(self.salario)
        return cadena

    def mostrarSalario(self):
        print("\nEl salario del {} es de: {}".format(self.__class__.__name__, self.salario))
        print("{}".format(self.calcularBonoAsistencia()))
