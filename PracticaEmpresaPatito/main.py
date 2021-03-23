from Empleados import Empleados
from Obreros import Obreros
from Administradores import Administradores
from Intendencia import Intendencia

if __name__ == '__main__':
    emps = [Obreros(5000, 28),Administradores(10000, 30),Administradores(10000, 25),Intendencia(5000, 30),
            Intendencia(5000, 25),Intendencia(5000, 20)]
    Administradores.numeroMetaAlcanzada = 5
    cuenta_intendentes = 0

    for emp in emps:
        emp.mostrarSalario()
        if isinstance(emp, Intendencia):
            cuenta_intendentes += 1
    if cuenta_intendentes < 3:
        print("Falta registrar a un intendente")
