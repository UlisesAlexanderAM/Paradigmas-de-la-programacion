class Operaciones3Numeros(Operaciones.Operaciones):
    def __init__(self, num1, num2, num3):
        super.num1 = num1
        super.num2 = num2
        self.num3 = num3

    def suma(self, num1, num2, num3):
        return num1, num2, num3

    def resta(self, num1, num2, num3):
        return num1, num2, num3

    def multiplicacion(self, num1, num2, num3):
        return num1 * num2 * num3

    def imprimirResultados(self):
        print("Numero 1: {}".format(self.num1))
        print("Numero 2: {}".format(self.num2))
        print("Numero 3: {}".format(self.num3))
        print("{} + {} + {} = {}".format(self.num1, self.num2, self.num3, self.suma(self.num1, self.num2, self.num3)))
        print("{} - {} - {} = {}".format(self.num1, self.num2, self.num3, self.resta(self.num1, self.num2, self.num3)))
        print("{} * {} * {} = {}".format(self.num1, self.num2, self.num3, self.multiplicacion(self.num1, self.num2,
                                                                                              self.num3)))
