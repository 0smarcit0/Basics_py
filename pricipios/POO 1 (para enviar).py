class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

Persona.nombre = "Pedro"
Persona.edad = 25
Persona.altura = 1.80
print(Persona.nombre)
print(Persona.edad)
print(Persona.altura)
print()
persona = Persona("Cristina", 23, 1.60)
print(persona.nombre)
print(persona.edad)
print(persona.altura)       
print()
persona1 = Persona("Manuel", 20, 1.74)
print(persona1.nombre)
print(persona1.edad)
print(persona1.altura)  
print()
persona2 = Persona("Maria", 30, 1.69)
print(persona2.nombre)
print(persona2.edad)
print(persona2.altura)  