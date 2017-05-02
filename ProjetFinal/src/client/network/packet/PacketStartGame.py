'''
Created on 8 fÃ©vr. 2017

@author: mathi
'''

class PacketStartGame():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par défault
    def __init__(self):
     
      self.main = None

    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau découper par le séparateur # recu dans Receiver
    def read(self, main, value):
        self.value = value
				
        self.main = main
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le méssage dans le tchat
    def handle(self):
        self.main.startGame(self.value)
        return self
