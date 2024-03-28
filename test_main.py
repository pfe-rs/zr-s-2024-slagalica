from klase import *

def test_resivo():
    tab = Tabla(3,3)
    matrica = [[1,2,3,4,5,6,7,8], [1,2,3,4,5,6,8,7], [2,1,3,4,5,6,7,8,0]]
    values = [True, False, False]
    for i in range(len(matrica)):
        assert Tabla.resivo(matrica[i]) == values[i]

def test_pomeri():
    tab = Tabla(3,3)

    table = [[1,2,3,4,5,6,7,8,0],[1,2,3,4,5,6,7,8,0],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8]]
    pokreti = ['left','up', 'right', 'down']
    values = [False, False, False, False]

    for i in range(4):
        tab.setTabla(table[i])
        assert tab.pomeri(pokreti[i]) == values[i]

def test_reseno():
    tab = Tabla(3,3)

    table = [[1,2,3,4,5,6,7,8,0],[0,1,2,3,4,5,6,7,8]]
    values = [True, False]

    for i in range(len(table)):
        tab.setTabla(table[i])
        assert tab.resena() != values[i]


