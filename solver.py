from klase import Tabla
import copy
from collections import defaultdict

class Cvor:
    def __init__(self, tabla:Tabla):
        self._val = tabla
    
    def getTabla(self):
        return self._val.getTabla()
    
    def getN(self):
        return self._val.getN()
    
    def getM(self):
        return self._val.getM()

    def nextMoves(self):
        moves = []
        for move in ['u', 'r', 'l', 'd']:
            tab = Tabla(3,3)
            tab.setTabla(copy.copy(self._val.getTabla()), self.getN(), self.getM())
            if tab.pomeri(move):
                moves.append((move, Cvor(tab)))
        return moves




class Solver:
    def __init__(self, start:Cvor):
        self._startPos = start

    @staticmethod
    def solve(startTab:Tabla):
        start = Cvor(startTab)
        temp = [i for i in range(1, start._val.getM()*start._val.getN())]
        temp.append(0)
        goal = tuple(temp)
        path = {}
        path[tuple(start._val.getTabla())] = []
        q = []
        visited = defaultdict(int)
        visited[tuple(start._val.getTabla())] += 1
        q.append(start)
        while(len(q)):
            current = q.pop(0)
            if tuple(current.getTabla()) == goal:
                return path[goal]
                
            for move in current.nextMoves():
                if visited[tuple(move[1].getTabla())] > 0:
                    continue
                path[tuple(move[1].getTabla())] = []
                path[tuple(move[1].getTabla())] += path[tuple(current.getTabla())]
                path[tuple(move[1].getTabla())]+= move[0]
                new = Cvor(copy.copy(move[1]))
                q.append(new)
                visited[tuple(move[1].getTabla())] += 1

'''
cvor = Cvor(Tabla(3,3))
print(cvor._val.getTabla(), 'ovo je koju tablu resava')
Solver.solve(cvor)
[4, 8, 3, 6, 7, 2, 1, 5, 0] ovo je koju tablu resava
['r', 'r', 'd', 'l', 'u', 'r', 
'd', 'd', 'l', 'u', 'l', 'u', 
'r', 'r', 'd', 'd', 'l', 'u', 
'r', 'u', 'l', 'd', 'l', 'u']
'''