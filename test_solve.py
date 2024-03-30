from solver import *

import random

def test_solve():    
    for _ in range(3):
        tab = Tabla(3,3)
        seq = Solver.solve(Cvor(tab))
        for move in seq:
            assert tab.pomeri(move)
        assert tab.resena()

    