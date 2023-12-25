def rectangulo(x,y):
    for i in range(x):
        for j in range(y):
            print("* ", end=" ")
        print("\n")

#parametro sep

x = int(input("altura: "))
y= int(input("ancho: "))

rectangulo(x,y)