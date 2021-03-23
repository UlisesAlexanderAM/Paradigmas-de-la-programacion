from Empleados import Empleados

class Intendencia(Empleados):
    def __init__(self,salario,dias_asistidos):
        super(Intendencia, self).__init__(salario,dias_asistidos)

    def mostrarSalario(self):
        super(Intendencia, self).mostrarSalario()
