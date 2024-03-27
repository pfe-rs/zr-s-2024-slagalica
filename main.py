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

    def resivo(self):
        return

    def izmesaj(self):
        tab = [i for i in range(1, self.n*self.m)]
        random.shuffle(tab)
        tab.append(0)
        self.tabla = tab
    
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

tab = Tabla(3,3)
