from klase import Tabla

class Cvor:
    def __init__(self, tabla:Tabla):
        self._val = tabla

class Solver:
    def __init__(self, start:Cvor):
        self._startPos = start
    