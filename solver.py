from klase import Tabla

class Cvor:
    def __init__(self, tabla:Tabla):
        self._val = tabla

class Solver:
    def __init__(self, start:Cvor):
        self._startPos = start

def bfs(self, start, goal):
        path = {}
        path[start] = []
        q = []
        visited = []
        visited.append(start)
        q.append(start)
        while(len(q)):
            current = q.pop(0)
            path[current] += {current}
            if current == goal:
                print(path[goal])
                return
            for v in self.vertices[current]:
                if v in visited:
                    continue
                path[v] = []
                path[v]+= path[current]
                q.append(v)
                visited.append(v)
    