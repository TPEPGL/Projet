#!/usr/bin/env python
# -*- coding: utf-8 -*-
class PacketPiege():
    '''
    classdocs
    '''

    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
        self.main = None
        self.x = 0
        self.y = 0
        self.id = 0
        self.type = 0
        
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main, type, x, y, id):
        self.main = main
        self.x = x
        self.y = y
        self.type = type
        self.id = id
        return self
    
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caract�re :
    #Exemple : 
    def write(self):
        if self.type == "remove":
            return self.main.protocolmap.getProtocol(self) + "#"+self.type+"#"+str(self.x)+"#"+str(self.y)
        elif self.type == "piege":
            return self.main.protocolmap.getProtocol(self) + "#"+self.type+"#"+str(self.id)

    def read(self, main, value):
        self.main = main
        self.x = value[1]
        self.y = value[2]
        self.id = value[3]
        return self

    def handle(self):
        if str(self.x)+"#"+str(self.y) not in self.main.game.piege:
            self.main.game.piege[str(self.x)+"#"+str(self.y)] = self.id

