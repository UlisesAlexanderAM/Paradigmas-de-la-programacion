from Empleados import Empleados


class Administradores(Empleados):
    # Numero de veces que se han vendido $100,000 en la empresa
    numeroMetaAlcanzada = 0;

    def __init__(self, salario,diasAsistidos):
        super(Administradores, self).__init__(salario,diasAsistidos)

    def calculaBono(self):
        return self.numeroMetaAlcanzada*500

    def mostrarSalario(self):
        super(Administradores, self).mostrarSalario()
        print("El salario despues del bono por cada $100,000 es: {}".format(self.salario+self.calculaBono()))
