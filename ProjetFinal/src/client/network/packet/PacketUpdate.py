'''
Created on 4 fÃ©vr. 2017

@author: mathi
'''

class PacketUpdate():
    '''
    classdocs
    '''

    #Initialisation de la class avec les variables par défault
    def __init__(self):
        self.id = -1
        self.main = None
        
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main):
        self.main = main
        return self
        
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caractère :
    #Exemple : 
    #Id du joueur = 23
    #Protocol de la class = 0
    
    # -> 0#23
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+str(self.main.id))
