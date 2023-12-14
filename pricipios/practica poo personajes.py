class personaje: 
    def __init__(self, name,fuerza,vida,inteligencia,defensa): #atributos de la plantilla
        self.name = name
        self.fuerza = fuerza
        self.vida = vida
        self.inteligencia = inteligencia
        self.defensa =  defensa
    
    def mostrar(self):                                         #mostrar atributos
        print(self.name)
        print(self.fuerza)
        print(self.vida)
        print(self.inteligencia)
        print(self.defensa)
    
    def estado(self):                                           #para saber si esta muerto(vida<=0) o vivo (vida>0)
        return self.vida>0
    
    def morir(self):                                            #si murio, seteamos la vida a 0 para no tener numeros negaivos y avisamos
        self.vida = 0 
        print(self.name,"ha muerto")
    
    def daño(self, enemigo): #calculo del daño 
        if self.fuerza <= enemigo.defensa:
            print("no ha ocurrido nada")
            return 0
        elif self.fuerza > enemigo.defensa:
         return self.fuerza - enemigo.defensa 
    
    def atacar(self, enemigo):                                   #para atacar, nos ayudamos del metodo daño, para restarlo a la vida del enemigo
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        if daño != 0:
         print(self.name, "ha golpeado a ",enemigo.name, "y ha inflingido", daño,"pts de daño" )
         if enemigo.estado():       #esto es para que no hayan numeros negativos
            print("la vida del ",enemigo.name, "es:", enemigo.vida)
         else:
            enemigo.morir()
        else:
            return 0 
            
        
    
class guerrero(personaje):
    def __init__(self, name, fuerza, vida, inteligencia, defensa,espada):
        super().__init__(name, fuerza, vida, inteligencia, defensa)
        self.espada = espada
    
    def cambio_arma(self):
        x = int(input("ingrese el tipo de arma que desea: (1)espada,8 de daño (2)hacha,9 de daño"))
        if x == 1:
            self.espada = 8
        elif x == 2:
            self.espada = 9
    
    def mostrar(self):
      super().mostrar()
      print(self.espada)
    
    def daño(self, enemigo):
        if self.fuerza * self.espada <=enemigo.defensa:
          print("no ha ocurrido nada")
          return 0
        else:
          return self.fuerza * self.espada - enemigo.defensa
      
    
      
      
class mago(personaje):
    def __init__(self, name, fuerza, vida, inteligencia, defensa,libro):
        super().__init__(name, fuerza, vida, inteligencia, defensa)       
        self.libro = libro
    def daño(self, enemigo):
        if self.inteligencia * self.libro <= enemigo.defensa:
          print("no ha ocurrido nada")
          return 0
        else:
         return self.inteligencia * self.libro -enemigo.defensa
    def mostrar(self):
        super().mostrar()
        print(self.libro)
        
        
    






mi_personaje=personaje("personaje", 10,100,10,10)
personaje2 = mago("papu", 10, 120,15,10, 3)
personaje1 = guerrero("guts", 16, 100, 10,10, 5)


def combate(personaje1,personaje2):
    while personaje1.estado() and personaje2.estado():
     personaje1.atacar(personaje2)
     personaje2.atacar(personaje1)
    if personaje1.estado():
        print("ha ganado", personaje1.name)
    elif personaje2.estado():
        print("ha ganado",personaje2.name)
    else:
        print("empate")
     
    


combate(personaje1, personaje2)