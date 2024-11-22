import math

if __name__ == '__main__':

    Suma = lambda x,y:x+y
    resultado = Suma(3,4)
    print(f"suma {resultado}")

    Potencia = lambda x:x**2
    print(f"potencia {Potencia(2)}")

    x1 = lambda a,b,c : (-b+(math.sqrt(b**2 *4*a*c)))/2*a
    x2 = lambda a,b,c : (-b-(math.sqrt(b**2 *4*a*c)))/2*a
    print(f"x1 {x1(6,19,7)}")
    print(f"x2 {x2(6,19,7)}")
