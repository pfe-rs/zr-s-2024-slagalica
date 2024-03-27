import random

class Tabla:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.izmesaj()
        self.nula = self.tabla.index(0)

    def provera(self):
        check = [i for i in range(1, self.n*self.m)]
        check.append(0)
        return check == self.tabla

    @staticmethod
    def resivo(tab):
        numOfInversions = 0
        length = len(tab)
        for i in range(length-1):
            for j in range(i+1, length):
                if tab[i] > tab[j]:
                    numOfInversions += 1
        return numOfInversions % 2 == 0

    def izmesaj(self):
        tab = [i for i in range(1, self.n*self.m)]
        while True:
            random.shuffle(tab)
            if Tabla.resivo(tab):
                tab.append(0)
                self.tabla = tab
                return
    
    def pomeri(self, smer):
        match smer:
            case('up'):
                if self.nula < self.m:
                    return False
                self.tabla[self.nula], self.tabla[self.nula - self.m] = self.tabla[self.nula - self.m], self.tabla[self.nula]
                self.nula = self.nula - self.m
                return True
            case('left'):
                if self.nula % self.m == 0:
                    return False
                self.tabla[self.nula], self.tabla[self.nula-1] = self.tabla[self.nula-1], self.tabla[self.nula]
                self.nula = self.nula - 1
                return  True
            case('right'):
                if self.nula % self.m == self.m-1:
                    return False
                self.tabla[self.nula], self.tabla[self.nula + 1] = self.tabla[self.nula + 1], self.tabla[self.nula]
                self.nula = self.nula + 1
                return True
            case('down'):
                if self.nula >= self.m*(self.n-1):
                    return False
                self.tabla[self.nula], self.tabla[self.nula + self.m] = self.tabla[self.nula + self.m], self.tabla[self.nula]
                self.nula = self.nula + self.m
                return True
            case _:
                return False

class CrtajTabla:
    @staticmethod
    def crtajTablu(tabla:Tabla):
        n = tabla.n
        m = tabla.m

        for i in range(n):
            for j in range(m):
                print("+---", end="")
            print("+")
            for j in range(m):
                print("| {} ".format(tabla.tabla[i * m + j]), end="")
            print("|")
        for j in range(m):
            print("+---", end="")
        print("+")

tab = Tabla(3,3)

''' World class testing
print(Tabla.resivo([1,2,3,4,5,6,7,8]))
print(Tabla.resivo([1,2,3,4,5,8,6,7]))
print(Tabla.resivo([1,2,3,4,5,6,8,7]))
'''

playing = True
while playing:
    CrtajTabla.crtajTablu(tab)
    a = input()
    if not tab.pomeri(a):
        print("Invalid input, try: up, left, right or down. And don't go out of the board.")
    
    if tab.provera():
        CrtajTabla.crtajTablu(tab)
        print("Congrats you won!!!")
        break
