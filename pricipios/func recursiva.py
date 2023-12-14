def regresiva(num):
    
    num-= 1
    if num > 0:
        regresiva(num)   
        return num
    


for x in range(6):
    x-=1
    print(regresiva(x))









"""def factorial(fact):
    if fact>0:
        valor=fact*factorial(fact-1)
        return valor
    else:
        return 1

print(f"El factorial de 4 es {factorial(4)}")"""

"""def fibonacci(n):
    if n == 0 or n ==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

fibonacci(0)"""

