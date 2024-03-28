import random

class Tabla:
    def __init__(self, n, m):
        self._n = n
        self._m = m
        self.izmesaj()
        self._nula = self._tabla.index(0)

    def resena(self):
        check = [i for i in range(1, self._n*self._m)]
        check.append(0)
        return check == self._tabla

    def setTabla(self, lista):
        self._tabla = lista

    @staticmethod
    def resivo(tab):
        numOfInversions = 0
        length = len(tab)
        for i in range(length-1):
            for j in range(i+1, length):
                if tab[i] > tab[j]:
                    numOfInversions += 1
        return numOfInversions % 2 == 0

    def getN(self):
        return self._n

    def getM(self):
        return self._m

    def getTabla(self):
        return self._tabla

    def izmesaj(self):
        tab = [i for i in range(1, self._n*self._m)]
        while True:
            random.shuffle(tab)
            if Tabla.resivo(tab):
                tab.append(0)
                self._tabla = tab
                return
    
    def pomeri(self, smer):
        match smer:
            case 'down' | 'd':
                if self._nula < self._m:
                    return False
                self._tabla[self._nula], self._tabla[self._nula - self._m] = self._tabla[self._nula - self._m], self._tabla[self._nula]
                self._nula = self._nula - self._m
                return True
            case 'right' | 'r':
                if self._nula % self._m == 0:
                    return False
                self._tabla[self._nula], self._tabla[self._nula-1] = self._tabla[self._nula-1], self._tabla[self._nula]
                self._nula = self._nula - 1
                return  True
            case 'left' | 'l':
                if self._nula % self._m == self._m-1:
                    return False
                self._tabla[self._nula], self._tabla[self._nula + 1] = self._tabla[self._nula + 1], self._tabla[self._nula]
                self._nula = self._nula + 1
                return True
            case 'up' | 'u':
                if self._nula >= self._m*(self._n-1):
                    return False
                self._tabla[self._nula], self._tabla[self._nula + self._m] = self._tabla[self._nula + self._m], self._tabla[self._nula]
                self._nula = self._nula + self._m
                return True
            case _:
                return False

class Igra:
    def __init__(self, tabla:Tabla):
        self._tabla = tabla

    def crtajTablu(self):
        n = self._tabla.getN()
        m = self._tabla.getM()
        tab = self._tabla.getTabla()

        for i in range(n):
            for j in range(m):
                print("+---", end="")
            print("+")
            for j in range(m):
                if tab[i*m + j] == 0:
                    val = ' '
                else:
                    val = str(tab[i*m + j])
                print("| {} ".format(val), end="")
            print("|")
        for j in range(m):
            print("+---", end="")
        print("+")
    
    def setTabla(self, list):
        self._tabla.setTabla(list)

    def pocniIgru(self):
        print("Use up(u), left(l), right(r) or down(d) to move a square int the empty slot.")
        playing = True
        while playing:
            self.crtajTablu()
            a = input()
            if not self._tabla.pomeri(a):
                print("Invalid input, try: up(u), left(l), right(r) or down(d). And don't go out of the board.")
            
            if self._tabla.resena():
                self.crtajTablu()
                print("Congrats you won!!!")
                break
