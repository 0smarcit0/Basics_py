def esmultiplo (x,y):
 a =x%y
 if a == 0:
     return True
 else:
     return False

 

a = int(input("Ingrese el numero: "))
b = int(input("Ingrese el numero del que quiere saber si es multiplo:  "))

z=esmultiplo(a,b)

if z == True:
    print(a,"es multiplo de",b)
else:
    print(a,"no es multiplo de",b) 