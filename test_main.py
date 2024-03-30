from klase import *

def test_resivo():
    tab = Tabla(3,3)
    matrica = [[1,2,3,4,5,6,7,8], [1,2,3,4,5,6,8,7], [2,1,3,4,5,6,7,8,0]]
    values = [True, False, False]
    for i in range(len(matrica)):
        assert Tabla.resivo(matrica[i]) == values[i]

def test_resivo_v2():
    tab = Tabla(3, 4)
    matrica = [[1,2,3,4,5,6,7,8,9,10,11], [1,2,3,4,5,6,8,7,9,10,11], [2,1,3,4,5,6,7,8,9,10,11]]
    values = [True, False, False]
    for i in range(len(matrica)):
        assert Tabla.resivo(matrica[i]) == values[i]


def test_pomeri():
    tab = Tabla(3,3)

    table = [[1,2,3,4,5,6,7,8,0], [1,2,3,4,5,6,7,8,0], [0,1,2,3,4,5,6,7,8], [0,1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]]
    pokreti = ['left', 'up', 'right', 'down','l', 'u']
    values = [False, False, False, False, False, False]
    dimN = [3,3,3,3,4,4]
    dimM = [3,3,3,3,4,4]

    for i in range(4):
        tab.setTabla(table[i], dimN[i], dimM[i])
        assert tab.pomeri(pokreti[i], input) == values[i]

def test_reseno():
    tab = Tabla(3,3)

    table = [[1,2,3,4,5,6,7,8,0],[0,1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]]
    values = [True, False,True]
    dimN = [3,3,4]
    dimM = [3,3,4]

    for i in range(len(table)):
        tab.setTabla(table[i], dimN[i], dimM[i])
        assert tab.resena() == values[i]

def pseudo_input(ulazi):
    def pseudo_get(): 
        for i in ulazi:
            yield i
    temp = pseudo_get()
    def pseudo_next():
        return next(temp)
    return pseudo_next

def test_citanje_upisivanje():
    tab = Tabla(3,3)
    A = Igra()
    #tablePomerene = [[0,5,6,3,4,2,1,8,7], [2,14,1,9,15,0,7,11,6,8,4,5,10,13,3,12], [11,0,4,2,10,9,1,3,7,8,6,5]]
    ulazi = [['old', 'test3x3','d','d','r','r', 'give up', 't3x3'], ['old','test4x4','d','d','r','r', 'something', 'give up', 't4x4'], ['old','test3x4','d','d','r','r', 'give up', 't3x4']]
    values = ['t3x3 3 3 0,5,6,3,4,2,1,8,7,', 't4x4 4 4 2,14,1,9,15,0,7,11,6,8,4,5,10,13,3,12,', 't3x4 3 4 11,0,4,2,10,9,1,3,7,8,6,5,']
    for i in range (len(values)-1):
        ulaz = ulazi[i]
        A.pocniIgru(pseudo_input(ulaz))
        f = open('allgames.txt', 'r')
        fread = f.read()
        f.close()
        assert fread.__contains__(values[i])
