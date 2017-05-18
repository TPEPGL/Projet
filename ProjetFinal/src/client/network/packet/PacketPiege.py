'''
Created on 8 févr. 2017

@author: mathi
'''

import time

class PacketPiege():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
        self.x = 0
        self.y = 0
        self.id = 0
        self.main = None
     
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caract�re :
    #Exemple : 
    #Protocol de la class = 2
    #Message � l'envoyer = "Salut toi"
    def init(self, main, x, y, id):
        self.main = main
        self.x = x
        self.y = y
        self.id = id
        return self
    # -> 2#Salut toi
    def write(self):
        return self.main.protocolmap.getProtocol(self) + "#" +str(self.x) + "#" + str(self.y) + "#" + self.id 
    
    
    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau d�couper par le s�parateur # recu dans Receiver
    def read(self, main, value):	
        self.main = main
        self.x = int(value[1])
        self.y = int(value[2])
        self.id = int(value[3])
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le message dans le tchat
    def handle(self):
        return self
