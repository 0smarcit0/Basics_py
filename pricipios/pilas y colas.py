pila = [1,2,3,4]

pila.append(5)

print(pila)

pila.pop()

print (pila)

from collections import deque #inportamos las caracteristicas de una cola 

cola= deque([1,2,3,4])
print(len(cola))
cola.append(7)
cola.appendleft(9)

print (cola)

cola.popleft()

print(cola)
 