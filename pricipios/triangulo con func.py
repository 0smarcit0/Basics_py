def triangulo1(x):
    a =1
    for i in range(x):
        for i in range(a):
         print("* ", end=" ")
        a+=1
        print()
        
def triangulo2(x):
    a=x-1
    for i in range(x):
        for i in range(a):
         print("* ", end=" ")
        a-=1
        print()
    triangulo1(x-1)
        


x = int(input("ancho: "))

triangulo1(x)
triangulo2(x)

        