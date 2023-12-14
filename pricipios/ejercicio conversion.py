
def cambio(x,y):
    if y == 1:
        return 35 * x
    elif y ==2:
        return x/35
    
a=int(input("de dolares a bs (1) \n de bs a dolares (2)\n"))

b=float(input("ingrese el monto que desea convertir: "))



if a==1:
    print("el monto es: ", cambio(b,a)," bs")
elif a ==2:
    print("el monto es: ", cambio(b,a)," dolares")