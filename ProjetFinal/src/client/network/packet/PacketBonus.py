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
        self.id2 = 0
        self.main = None
     
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
        if self.type == "remove":
            self.id = int(value[4])
            self.id2 = int(value[5])
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le message dans le tchat
    def handle(self):
        
        if (self.type == "pose"):
            self.main.fenetregame.canvas.itemconfig(self.main.fenetregame.listitem[self.x][self.y], image = self.main.image["bonus"])
            self.main.fenetregame.listpiege.append(self.main.fenetregame.listitem[self.x][self.y])
        elif(self.type == "remove"):
            self.main.fenetregame.listpiege.remove(self.main.fenetregame.listitem[self.x][self.y])
            self.main.fenetregame.canvas.itemconfig(self.main.fenetregame.listitem[self.x][self.y], image = self.main.image["sol"])
            if (self.id == self.main.id):
                print("test")
        
        return self
