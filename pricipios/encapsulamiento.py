class Persona:
    def __init__(self, nom):
        self.__nom = nom
    def get_nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom

"""persona = Persona("Jose")
print(persona.get_nom())
persona = Persona("Ricardo")
print(persona.get_nom())"""

persona = Persona("jose")
print(persona.get_nom())

persona =Persona("osmar")
print(persona.get_nom())

