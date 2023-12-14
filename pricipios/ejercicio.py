
Lista = [1, 2, 3, 4, 5, 1, 6, 7, 9, 4, 5, 1, 8, 4, 1, 5]

aux ={
    
}
    

lista1 = []

for i in range(len(Lista)):
    if Lista[i] in aux:
        continue 
    else:
        aux[Lista[i]] = 1
        lista1.append(Lista[i])
         
print(lista1)      
            












