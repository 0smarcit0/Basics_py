class taza:
    def __init__(self, volumen, contenido, cantidad):
        self.volumen = volumen
        self.contenido = contenido
        self.cantidad = cantidad 
    def beber(self):
        if self.cantidad == False:
            print("la taza esta vacia")
        else:
         print("haz vevido")
         self.cantidad = False
               
    def rellenar(self):
        if self.cantidad == True:
            print("la taza ya esta llena")
        elif self.cantidad == False:
            self.cantidad = True 
            print("la rellenaste")




taza1 =taza(5, "cafe", True)

def accion():
    x = int(input("que desea hacer?: beber(1) rellenar(2) "))
    if x ==1:
        taza1.beber()
    elif x ==2:
        taza1.rellenar()
    
    z = int(input("desea seguir?: si(1) no(2)"))
    if z == 1:
        accion()
    elif z == 2:
        return 0
    
accion()

taza1.contenido = "agua"
print(taza1.contenido)