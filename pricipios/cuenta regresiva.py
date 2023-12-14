
def regresivo(n):
    n-=1
    if n > 0:
        regresivo(n)
        return n
        
    

    

 
for i in range(5): 
 num = regresivo(i)
 print(num)        
