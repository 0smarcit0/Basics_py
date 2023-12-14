def factorial(n):
    if n ==1:
        return n
    else:
        return n * factorial(n-1)
    
    
fact=factorial(7)
print(fact)