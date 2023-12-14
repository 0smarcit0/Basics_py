x = int(input("ingrese el numero: "))
y = int(input("ingrese el numero: "))
z = int(input("ingrese el numero: "))

if x>y and x>z:
    print("el mayor es: ", x )
elif y>x and y>z: 
    print("el mayor es: ", y )
elif z>x and z>y: 
    print("el mayor es: ", z )
else: 
    print("hay un empate") 

 