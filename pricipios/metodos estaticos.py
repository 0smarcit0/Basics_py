class Clase:
    var = "cubiwlet"
    def __init__(self):
        self.var_instancia =3
    
    def metodo3(self):
        self.metodo_propio()
        self.metodo2()
        print(self.var_instancia)
    
    @staticmethod
    def metodo_propio():
        print("hola")
        print(Clase.var)
        #print(Clase.var_instancia)
    
    @classmethod 
    def metodo2(cls):
        print("segunda forma de crear metodos estaticos")
        print(cls.var)
        
    

Clase.metodo_propio()
Clase.metodo2()
objeto = Clase()
print(objeto.metodo3())