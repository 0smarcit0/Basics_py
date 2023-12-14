from jugador_poli import Jugador

class equipo(Jugador):
    def __init__(self, nombre, posicion, equipo):
        super().__init__(nombre, posicion)
        self.equipo = equipo
    
    def __str__(self):
        return super().__str__() + " equipo: " + self.equipo
    