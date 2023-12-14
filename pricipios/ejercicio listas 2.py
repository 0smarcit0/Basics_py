Lista1 = [{2, 5, 89.3, "hola"}, {96, 1.2, 6, "adios"}, {"hora", 7, 9, 96, 1.3}, {"adios", 2, 1.2}]
Lista2 = [{1.2, "Venezuela", 2}, {"hola", 96, 8}, {42, 6.9, 96, 3, "hora"}, {12, 89.3, 8, 45, "te"}]

aux = set()
aux1 = set()
lista1=[]
lista2=[]
lista3=[]
lista4=[]


#primera parte
for i in Lista1:
    for x in i:
        for i in Lista2:
            if x in i:
                aux.add(x)
            
                    
for i in aux:
    lista1.append(i)

print(lista1)

aux.clear() #vaciamos aux

#segunda parte y tercera parte 

for i in Lista1:
    for x in i:
        aux.add(x)


for i in Lista2:
    for x in i:
        aux1.add(x)
                    
aux2 = aux - aux1
aux3 = aux1 - aux
                       
for i in aux2:
    lista2.append(i)

for i in aux3:
    lista3.append(i)
print(lista3)

print(lista2)

aux4 = aux2 | aux3

for i in aux4:
    lista4.append(i)

print(lista4)                    


            
        
                
                
                
        

        
     
    






