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
        self.type = 0
     
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
        self.type = value[1]
        if self.type == "remove":
            self.x = int(value[2])
            self.y = int(value[3])
        elif self.type == "piege":
            self.id = int(value[2])
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le message dans le tchat
    def handle(self):
        if self.type == "remove":
            if self.main.fenetregame.listitem[self.x][self.y] in self.main.fenetregame.listpiege:
                self.main.fenetregame.listpiege.remove(self.main.fenetregame.listitem[self.x][self.y])
                if self.main.fenetregame.listitem[self.x][self.y] in self.main.fenetregame.maptemp:
                    self.main.fenetregame.canvas.itemconfig(self.main.fenetregame.listitem[self.x][self.y], image = self.main.image["sol"])
                else:
                    self.main.fenetregame.canvas.itemconfig(self.main.fenetregame.listitem[self.x][self.y], image = self.main.image["solsombre"])
        elif self.type == "piege":
            if self.id == 0:
                self.main.taskpiege.startpiege0()
            elif self.id == 1:
                self.main.taskpiege.startpiege1()
        return self
