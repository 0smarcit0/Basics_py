tupla =((("a", "b"), ("c","d")), (("e","f"), ("g", "h")), (("i", "j"), ("k", "l")))

lista1 = []
lista2 = []
descom1 = []
descom2 = []
for x in tupla:
    for y in x:
        descom1.append(y[0])
        descom2.append(y[1])
        lista1.append(descom1)
        lista2.append(descom2)
        descom2=[]
        descom1=[]

print(lista1)
print(lista2)


tupla2 = ("a", "a", "b", "c", "d")

acumulador = 0
listaacumulada = []
listacomprimida = []

for i in range(len(tupla2)):
    if i + 1 < (len(tupla2)) and tupla2[i] == tupla2[i+1]:
        acumulador +=1
        listaacumulada = [acumulador, tupla2[i]]
        continue
    if listaacumulada:
        listaacumulada [0]+=1
        listacomprimida.append(listaacumulada)
        listaacumulada = []
        acumulador = 0
    else:
        listacomprimida.append(tupla2[i])
     
     
print(listacomprimida)     
    
        
