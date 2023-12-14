cuenta = 1000
x = 1
print("Cajero. \n")  
while x == 1:
 a = int(input("Que desea hacer? \n 1) Depositar(1) \n 2) Retirar(2) \n 3) Mostrar saldo(3) \n 4) Salir(4) \n "))
 if a == 1:
     monto= int(input("Ingrese la cantidad que desea depositar: "))
     cuenta +=monto
     print(cuenta)
     x = int(input("Desea realizar mas acciones? \n Si(1) \n No(4)"))
     if x == 4: 
         break
    
 elif a == 2:
         monto = int(input("Cuanto desea retirar?: "))
         if monto > cuenta:
             print("La cantidad que usted quiere retirar excede la que hay en la cuenta.")
             x = int(input("Desea realizar mas acciones? \n Si(1) \n No(4)"))
             if x == 4: 
              break
         else: 
            cuenta -= monto 
            print("ha retirado: ", monto, "en la cuenta ha quedado: ", cuenta)
            x = int(input("Desea realizar mas acciones? \n Si(1) \n No(4)"))
            if x == 4: 
                break 
 elif a == 3:
         print(cuenta)
         x = int(input("Desea realizar mas acciones? \n Si(1) \n No(4)"))
         if x == 4: 
          break        
 elif a == 4:
         break     
             
         

print("Hasta luego.")     
     