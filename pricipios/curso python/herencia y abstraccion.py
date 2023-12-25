from abc import ABC, abstractmethod
class jordan(ABC):
    def __init__(self, manejo, tiro, dunk):
        self.__manejo = manejo
        self.__tiro = tiro
        self.__dunk = dunk
    def __str__(self):
        return "manejo de balon: " + str(self.__manejo) + " tiro de media: " + str(self.__tiro) + " dunk: " + str(self.__dunk)
    def get_manejo(self):
        return self.__manejo
    def set_manejo(self, manejo):
        self.__manejo = manejo 
    
    def get_tiro(self):
        return self.__tiro
    def set_tiro(self, tiro):
        self.__tiro = tiro
        
    def get_dunk(self):
        return self.__dunk
    def set_dunk(self, dunk):
        self.__dunk = dunk  
    
    @abstractmethod
    def media(self):
        pass 



class bryant(jordan):
    def __init__(self, manejo, tiro, dunk,tiro3):
        super().__init__(manejo, tiro, dunk)
        self.tiro3 = tiro3
    def __str__(self):
        return super().__str__() + " tiro de 3: " + str(self.tiro3)
    def media(self):
        return (self.get_dunk()+self.get_manejo()+self.get_tiro()+self.tiro3)/4


class james(bryant, jordan):
    def __init__(self, manejo, tiro, dunk, tiro3,pasador):
        jordan.__init__(self,manejo,tiro,dunk)
        bryant.__init__(self,manejo, tiro, dunk, tiro3)
        self.pasador =pasador 
    def __str__(self):
        return super().__str__() + "pases: "+ str(self.pasador)
    
    def media(self):
        return (self.get_dunk()+ self.get_manejo()+ self.pasador+ self.get_tiro()+ self.tiro3)/5 #super().media()







kobe = bryant(8,8,8,6)
lebron = james(8,8,10,7,8)
print(kobe)
print(kobe.media())
print(lebron)
print(lebron.media())



