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

    def setTabla(self, lista, n, m):
        self._tabla = lista
        self._n = n
        self._m = m
        self._nula = self._tabla.index(0)

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
                if self.resena():
                    continue
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
            case 'give up':
                print("Give your game a name:\n")
                name = input()
                name = (name.translate({ord(i): None for i in ' '}))
                f = open('allgames.txt', 'a')
                f.write('%s ' %name)
                f.write('%d ' %self._n)
                f.write('%d ' %self._m)
                for items in self._tabla:
                    f.write('%s,' %items)
                f.write('\n')
                f.close()
                return False
            case _:
                return False

class Igra:
    
    def __init__(self):
        self._tabla = Tabla(3,3)
    

    def crtajTablu(self):
        n = self._tabla.getN()
        m = self._tabla.getM()
        tab = self._tabla.getTabla()

        max_width = len(str(max(tab)))
        lines = (2+max_width) * '-'


        for i in range(n):
            for j in range(m):
                print("+", end="")
                print(lines, end="")
            print("+")
            for j in range(m):
                if tab[i*m + j] == 0:
                    val = ' ' * max_width
                else:
                    val = str(tab[i*m + j]).rjust(max_width)
                print("|", end="")
                print(" {} ".format(val), end="")
            print("|")
        for j in range(m):
            print("+", end="")
            print(lines, end="")
        print("+")

    def setTabla(self, list, n, m):
        self._tabla.setTabla(list, n, m)

    def pocniIgru(self, input_fn):
        print ("To start a new game enter new, to choose an old game to continue enter old.")
        choice = input_fn()
        if choice == 'old':
            print("Enter the name of the game you want to play:")
            f = open('allgames.txt', 'r')
            fread = f.read()
            games = list(fread.split('\n'))
            names = list(fread.split('\n'))
            for i in range (len(games)-1):
                names[i], sep, tail = games[i].partition(' ')
                #[i] = values[i][0:-1]              
                print(names[i])
            f.close()
            decision = input_fn()
            if decision in names:
                indx = names.index(decision)
                names[indx], sep, tail = games[indx].partition(' ')
                n, sep, tail = tail.partition(' ')
                m, sep, tail = tail.partition(' ')
                n = int(n)
                m = int(m)
                values = list(tail.split(','))
                values = values[0:-1]
                values = list(map(int, values))
                self.setTabla(values, n, m)
            else:
                print ("Please enter a valid game name.")
                self.pocniIgru()
        if choice == 'new':
            n, m = map(int, input_fn("Enter dimensions separated by a space: ").split())
            tab = Tabla(n,m).getTabla()
            self.setTabla(tab, n, m)
        if choice != 'new' and choice != 'old': 
            self.pocniIgru(input)

        print("Use up(u), left(l), right(r) or down(d) to move a square intogive  the empty slot.\nTo give up and save your game, enter give up.")
        playing = True
        while playing:
            self.crtajTablu()
            a = input_fn()
            if not self._tabla.pomeri(a):
                if (a == 'give up'):
                    print("Game stopped, better luck next time, loser.")
                    break
                print("Invalid input, try: up(u), left(l), right(r) or down(d). And don't go out of the board.")
            
            if self._tabla.resena():
                self.crtajTablu()
                print("Congrats you won!!!")
                break
