class animalitos:
    def __init__(self, patas, tipo, animal):
        self.patas = patas
        self.tipo = tipo
        self.animal = animal
    def __str__(self):
        return "tipo "+ self.tipo + "animal "+self.animal+"patas: "+str(self.patas)