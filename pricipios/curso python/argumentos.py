def multi(x):
    x *= 2
    print("la multiplicacion es:", x)

n = 5

multi(n)

a = [2,3,6]

def multi(numeros):
    for i in range(len(numeros)):
        numeros[i]*= 2
    return numeros

b = multi(a)

print(b)