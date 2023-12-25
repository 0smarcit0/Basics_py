class Animal:
    def __init__(self, tipo, animal, patas):
        self.tipo = tipo
        self._animal = animal
        self.__patas = patas
        
    def get_patas(self):          #protegemos el atributo patas
        return self.__patas
    def set_patas(self,patas):
        self.__patas = patas
    
    def get_animal(self):          #protegemos el atributo animal
        return self._animal
    def set_animal(self,animal):
        self._animal = animal
        
    def __mostrar(self):           #creamos el metodo privado para mostrar 
        print(self.tipo)
        print(self._animal)
        print(self.__patas) 
    def acceso(self):              #creamos el metodo publico 
        self.__mostrar()

        


animal = Animal("domestico", "perro", 4)
animal.acceso()


an1 = Animal("salvaje","tigre",4)
an1.acceso()


an1.set_animal("oso")
print(an1.get_animal())

