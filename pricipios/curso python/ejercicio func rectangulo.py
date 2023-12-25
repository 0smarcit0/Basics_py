def rectangulo(x,y,z):
    for i in range(x):
        for j in range(y):
            print(z, end=" ")
        print("\n")

#parametro sep

x = int(input("altura: "))
y= int(input("ancho: "))
z = input("ingrese el caracter que desea imprimir: ")

rectangulo(x,y,z)