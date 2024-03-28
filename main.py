import random
from klase import *

n, m = map(int, input("Enter dimensions separated by a space: ").split())

tab = Tabla(n,m)

''' World class testing
print(Tabla.resivo([1,2,3,4,5,6,7,8]))
print(Tabla.resivo([1,2,3,4,5,8,6,7]))
print(Tabla.resivo([1,2,3,4,5,6,8,7]))
'''

igra = Igra(tab)
igra.pocniIgru()