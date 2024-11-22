class general:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def x1 (self)-> float:
        r = self.b**2-(4*(self.a * self.c))
        x1=(-self.b+r**0.5)/(2*self.a)
        return x1
    def x2 (self)-> float:
        r =self.b**2-(4*(self.a * self.c))
        x2=(-self.b-r**0.5)/(2*self.a)
        return x2

if __name__ == '__main__':
    resultado = general(6,19,7)
    print(f"x1= {resultado.x1()}")
    print(f"x1= {resultado.x2()}")