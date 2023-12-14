class Clase:
    var = "hola"
    def __init__(self,num):
        self.num = num

print(Clase.var)
objeto = Clase(1)

print(objeto.num)
print(objeto.var)
objeto.var = "chao"
print(objeto.var)