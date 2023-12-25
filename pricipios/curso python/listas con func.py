def numero():
    x = int(input("ingrese el tamaño: "))
    lis=lista(x)
    return lis



def lista(n):
    Lista = []
    for i in range(n):
        palabra=input("ingrese la palabra: ")
        Lista.append(palabra)
    return Lista
        
p=numero()

print(p)


