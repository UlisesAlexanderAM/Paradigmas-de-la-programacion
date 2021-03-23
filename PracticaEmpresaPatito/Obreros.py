from Empleados import Empleados


class Obreros(Empleados):

    def __init__(self, salario, dias_asistidos):
        super(Obreros, self).__init__(salario, dias_asistidos)

    def mostrarSalario(self):
        super(Obreros, self).mostrarSalario()

