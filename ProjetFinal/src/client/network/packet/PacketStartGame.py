'''
Created on 8 févr. 2017

@author: mathi
'''

class PacketStartGame():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
     
      self.main = None

    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau d�couper par le s�parateur # recu dans Receiver
    def read(self, main, value):
        self.value = value
				
        self.main = main
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le m�ssage dans le tchat
    def handle(self):
        self.main.startGame(self.value)
        return self
