'''
Created on 8 févr. 2017

@author: mathi
'''

import time

class PacketBonus():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
        self.x = 0
        self.y = 0
        self.type = ""
        self.id = 0
        self.id2 = 0
        self.main = None
     
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caract�re :
    #Exemple : 
    #Protocol de la class = 2
    #Message � l'envoyer = "Salut toi"
    def init(self, main, type, x, y, id, id2):
        self.main = main
        self.type = type
        self.x = x
        self.y = y
        self.id = id
        self.id2 = id2
        return self
    # -> 2#Salut toi
    def write(self):
        return self.main.protocolmap.getProtocol(self) + "#" + self.type + "#" + str(self.x) + "#" + str(self.y) + "#" + self.id + "#" + str(self.id2)
    
    
    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau d�couper par le s�parateur # recu dans Receiver
    def read(self, main, value):
        self.type = value[1]
        self.main = main
        self.x = int(value[2])
        self.y = int(value[3])
        if self.type == "remove" or self.type == "bonus1":
            self.id = int(value[4])
            self.id2 = int(value[5])
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le message dans le tchat
    def handle(self):

        print(self.type + "#" + str(self.x) + "#" + str(self.y) + "#" + str(self.id) + "#" + str(self.id2))
        if self.type == "pose":
            self.main.fenetregame.canvas.itemconfig(self.main.fenetregame.listitem[self.x][self.y], image = self.main.image["bonus"])
            self.main.fenetregame.listpiege.append(self.main.fenetregame.listitem[self.x][self.y])
        elif self.type == "remove":
            if self.main.fenetregame.listitem[self.x][self.y] in self.main.fenetregame.listpiege:
                self.main.fenetregame.listpiege.remove(self.main.fenetregame.listitem[self.x][self.y])
                if self.main.fenetregame.listitem[self.x][self.y] in self.main.fenetregame.maptemp:
                    self.main.fenetregame.canvas.itemconfig(self.main.fenetregame.listitem[self.x][self.y], image = self.main.image["sol"])
                else:
                    self.main.fenetregame.canvas.itemconfig(self.main.fenetregame.listitem[self.x][self.y], image = self.main.image["solsombre"])
                if str(self.id) == self.main.id:
                    if self.id2 == 0:
                        self.main.taskbonus.startbonus0()
                    if self.id2 == 1:
                        self.main.taskbonus.startbonus1()
                elif self.id2 == 1:
                    print("dd")
                    if self.id not in self.main.fenetregame.invilist:
                        print("ddd")
                        self.main.fenetregame.invilist.append(self.id)
                        self.main.fenetregame.canvas.tag_lower(self.main.fenetregame.other[self.id][3])
        elif self.type == "bonus1" and str(self.id) != self.main.id:
            print("dd2")
            if self.id in self.main.fenetregame.invilist:
                self.main.fenetregame.invilist.remove(self.id)
            if self.id in self.main.fenetregame.findlist:
                self.main.fenetregame.canvas.tag_raise(self.main.fenetregame.other[self.id][3])
        return self
