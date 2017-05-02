'''
Created on 7 fÃ©vr. 2017

@author: mathi
'''
from time import time
class PacketTest():
    '''
    classdocs
    '''

    #Initialisation de la class avec les variables par défault
    def __init__(self):
        self.time = 0
        self.main = None
        
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main):
        self.main = main
        return self
        
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caractère :
    #Exemple : 
    #Id du joueur = 23
    #Protocol de la class = 1
    #l'heure en miliseconde de la machine = "234567890"
    
    # -> 3#23#234567890
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+str(self.main.id)+"#"+str(time()))
    
    
    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau découper par le séparateur # recu dans Receiver
    def read(self, main, value):
        self.time = float(value[2])
        self.main = main
        return self
        
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le temps recu dans le tchat en enlever 
    #l'heure en miliseconde de la machine
    #Ce qui nous donnera le temps en miliseconde qui sera le temps pour que le méssage fasse un aller retour
    def handle(self):
        self.main.sendMessage(str((time() - self.time)*1000) + " ms")
        return self
