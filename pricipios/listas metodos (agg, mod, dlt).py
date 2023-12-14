lista = [2,3,2.5,4.564, "waza", True]
lista2 = [3,5]
for i in lista:
    print(i) 

print(lista[4])
print(lista[:4]) 

lista.append(False) #añadir elemento al final de la lista, tambien funciona con introducir otras listas
lista.append([2,"hi"])
print(lista)

lista.extend(lista2) #volver elementos de una lista a propios de otra lista
print(lista)

lista.remove(4.564)
print(lista)

lista.reverse()
print(lista)

a = lista.index([2,"hi"])
print(a)

b = lista.count(3)
print(b)