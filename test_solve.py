from klase import *

def test_solve():    
    for _ in range(3):
        tab = Tabla(3,3)
        seq = Igra.solve(Cvor(tab),input)
        for move in seq:
            assert tab.pomeri(move, input)
        assert tab.resena()

    