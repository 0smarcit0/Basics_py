def menu():
    print(".MENÚ DE OPCIONES.\n 1)Agregar nuevo. \n 2)Mostrar todos \n 3)Mostrar por DNI \n 4)Eliminar \n 5)Salir")
    x = int(input("¿Que desea realizar?: "))
    if x ==1:
        añadir()
    elif x == 2:
        mostrar()
    elif x==3:
        mostrardni()
    elif x == 4:
        eliminar()
    elif x == 5:
        return 0
    
clientes = {"USER0":"USER0"}
    
def añadir():
    x = input("ingrese el dni del cliente: ")
    y = input("ingrese el nombre y apellido: ")
    clientes[x] = y
    z = int(input("desea agregar otro cliente? Si(1) No(2)"))
    if z == 1:
        añadir()
    elif z == 2:
        menu()
    

def mostrar():
    for i in clientes:
        print(clientes[i]) 
    
    x = int(input("desea hacer algo mas? SI(1) No(2)"))
    if x == 1:
        menu()
    else:
        return 0
 


def mostrardni():
    x = input("ingrese el DNI del cliente: ")
    if x in clientes:
        print(clientes[x])
    else:
        print("no existe un cliente con ese DNI")
    
    z = int(input("desea mostrar otro cliente? SI(1) No(2)"))
    if z == 1:
        mostrardni()
    else:
        menu()
    
    
def eliminar():
    x = input("ingrese el dni del cliente que desea eliminar: ")
    if x in clientes:
        clientes.pop(x)
    else: 
        print("no hay un cliente con esa DNI")
    
    z = int(input("desea eliminar otro cliente? SI(1) No(2)"))
    if z == 1:
        eliminar()
    else:
        menu()




menu()