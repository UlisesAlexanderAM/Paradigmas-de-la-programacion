from Punto import Punto
from Linea import Linea
from Rectangulo import Rectangulo

if __name__ == '__main__':
    punto_a = Punto(0,2)
    punto_b = Punto(2,0)
    linea_1 = Linea()
    linea_2 = Linea(punto_a,punto_b)
    linea_1.mostrarLinea()
    linea_2.mostrarLinea()
    linea_1.mueveDerecha(2)
    linea_1.mostrarLinea()
    linea_1.mueveIzquierda(2)
    linea_1.mostrarLinea()
    linea_2.mueveAbajo(5)
    linea_2.mostrarLinea()
    linea_2.mueveArriba(5)
    linea_2.mostrarLinea()
