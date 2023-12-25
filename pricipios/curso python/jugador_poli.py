class Jugador:
    def __init__(self,nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion
    def __str__(self):
        return "nombre: "+ self.nombre + " posicion: "+self.posicion