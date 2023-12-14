def fibonacci(x):
    if x == 0 or x == 1:
        return 1 
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    
    



x = 5
for i in range(x):
    print(fibonacci(i))





    