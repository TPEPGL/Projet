'''
Created on 8 fÃ©vr. 2017

@author: mathi
'''

from tkinter import *
class PacketMove():
    '''
    classdocs
    '''
    # Initialisation de la class avec les variables par défault
    def __init__(self):
        self.main = None
        self.x = -1
        self.y = -1
        
    # Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main, x, y):
        self.main = main
        self.x = x
        self.y = y
        return self
        
    # Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caractère :
    # Exemple : 
    # Protocol de la class = 2
    # Message à l'envoyer = "Salut toi"
    
    # -> 2#Salut toi
    def write(self):
        return (self.main.protocolmap.getProtocol(self) + "#" + str(self.main.id) + "#" + str(self.x) + "#" + str(self.y))
    
    
    # Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau découper par le séparateur # recu dans Receiver
    def read(self, main, value):
        self.id = int(value[1])
        self.x = int(value[2])
        self.y = int(value[3])
        self.main = main
        return self
        
    # Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le méssage dans le tchat
    def handle(self):
        if self.id == int(self.main.id):
            self.main.fenetregame.canvas.move(self.main.fenetregame.Pion, self.y - self.main.fenetregame.posy, self.x - self.main.fenetregame.posx)
            self.main.fenetregame.posx = self.x
            self.main.fenetregame.posy = self.y
            map = []
            map.append(self.main.fenetregame.listitem[int(self.x / 22)][int(self.y / 22)])
            
            if (self.main.game.map[int((self.x + 22) / 22)][int(self.y / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int(self.y / 22)])
                if (self.main.game.map[int((self.x + 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int((self.y + 22) / 22)])
                if (self.main.game.map[int((self.x + 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int((self.y - 22) / 22)])
                if (self.main.game.map[int((self.x + 44) / 22)][int(self.y / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x + 44) / 22)][int((self.y) / 22)])
                    if (self.main.game.map[int((self.x + 66) / 22)][int(self.y / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x + 66) / 22)][int((self.y) / 22)])
                    if (self.main.game.map[int((self.x + 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int((self.x + 44) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x + 44) / 22)][int((self.y - 22) / 22)]) 
                    if (self.main.game.map[int((self.x + 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int((self.x + 44) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x + 44) / 22)][int((self.y + 22) / 22)])   
                       
                        
            if (self.main.game.map[int((self.x - 22) / 22)][int(self.y / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int(self.y / 22)])
                if (self.main.game.map[int((self.x - 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int((self.y + 22) / 22)])
                if (self.main.game.map[int((self.x - 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int((self.y - 22) / 22)])
                if (self.main.game.map[int((self.x - 44) / 22)][int(self.y / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x - 44) / 22)][int(self.y / 22)]) 
                    if (self.main.game.map[int((self.x - 66) / 22)][int(self.y / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x - 66) / 22)][int(self.y / 22)]) 
                    if (self.main.game.map[int((self.x - 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int((self.x - 44) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x - 44) / 22)][int((self.y - 22) / 22)]) 
                    if (self.main.game.map[int((self.x - 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int((self.x - 44) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x - 44) / 22)][int((self.y + 22) / 22)]) 
                           
            if (self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y + 22) / 22)])
                if (self.main.game.map[int(self.x / 22)][int((self.y + 44) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y + 44) / 22)])
                    if (self.main.game.map[int(self.x / 22)][int((self.y + 66) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y + 66) / 22)])
                    if (self.main.game.map[int((self.x - 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int((self.x - 22) / 22)][int((self.y + 44) / 22)] == 0 and self.main.game.map[int((self.x-22) / 22)][int((self.y) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int((self.y + 44) / 22)])
                    if (self.main.game.map[int((self.x + 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int((self.x + 22) / 22)][int((self.y + 44) / 22)] == 0 and self.main.game.map[int((self.x+22) / 22)][int((self.y) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int((self.y + 44) / 22)])
                
            if (self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y - 22) / 22)])
                if (self.main.game.map[int(self.x / 22)][int((self.y - 44) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y - 44) / 22)])
                    if (self.main.game.map[int(self.x / 22)][int((self.y - 66) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y - 66) / 22)])
                    if (self.main.game.map[int((self.x - 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int((self.x - 22) / 22)][int((self.y - 44) / 22)] == 0 and self.main.game.map[int((self.x-22) / 22)][int((self.y) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int((self.y - 44) / 22)])
                    if (self.main.game.map[int((self.x + 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int((self.x + 22) / 22)][int((self.y - 44) / 22)] == 0 and self.main.game.map[int((self.x+22) / 22)][int((self.y) / 22)] == 0):
                        map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int((self.y - 44) / 22)])
                        
                        
            for a in self.main.fenetregame.maptemp:
                if (a not in map):
                    self.main.fenetregame.canvas.itemconfig(a, image=self.main.image["solsombre"])
            for b in map:
                self.main.fenetregame.canvas.itemconfig(b, image=self.main.image["sol"])
            self.main.fenetregame.maptemp = map
            for b in self.main.fenetregame.other:
                if (self.main.fenetregame.listitem[int((self.main.fenetregame.other[b][0]) / 22)][int((self.main.fenetregame.other[b][1]) / 22)] in self.main.fenetregame.maptemp):
                    self.main.fenetregame.canvas.tag_raise(self.main.fenetregame.other[b][3])
                    if b  not in self.main.fenetregame.findlist:
                        self.main.fenetregame.findlist.append(b)
                else:
                    self.main.fenetregame.canvas.tag_lower(self.main.fenetregame.other[b][3])
                    if b in self.main.fenetregame.findlist:
                        self.main.fenetregame.findlist.remove(b)
        else:
            info = self.main.fenetregame.other[self.id]
            self.main.fenetregame.canvas.move(info[3], self.y - info[1], self.x - info[0])
            self.main.fenetregame.other[self.id][0] = self.x
            self.main.fenetregame.other[self.id][1] = self.y
            if (self.main.fenetregame.listitem[int((self.x) / 22)][int((self.y) / 22)] in self.main.fenetregame.maptemp):
                self.main.fenetregame.canvas.tag_raise(info[3])
                if self.id not in self.main.fenetregame.findlist:
                    self.main.fenetregame.findlist.append(self.id)
            else:
                self.main.fenetregame.canvas.tag_lower(info[3])
                if self.id in self.main.fenetregame.findlist:
                    self.main.fenetregame.findlist.remove(self.id)
        return self
