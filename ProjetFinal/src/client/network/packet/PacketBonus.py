'''
Created on 8 fÃ©vr. 2017

@author: mathi
'''

import time

class PacketBonus():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par défault
    def __init__(self):
        self.x = 0
        self.y = 0
        self.type = ""
        self.id = 0
        self.main = None
     
        
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main, type, id, x, y):
        self.main = main
        self.x = x
        self.y = y
        self.type = type
        self.id = id
        return self
        
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caractère :
    #Exemple : 
    #Protocol de la class = 2
    #Message à l'envoyer = "Salut toi"
    
    # -> 2#Salut toi
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.type)
    
    
    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau découper par le séparateur # recu dans Receiver
    def read(self, main, value):
        self.type = value[1]
        self.main = main
        self.x = int(value[2])
        self.y = int(value[3])
        self.id = int(value[4])
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le message dans le tchat
    def handle(self):
        self.main.fenetregame.listitem[self.x][self.y] = self.main.fenetregame.canvas.create_image(self.y+11,self.x+11,image=None)
        return self
