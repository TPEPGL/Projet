#!/usr/bin/env python
# -*- coding: utf-8 -*-
class PacketInfoGame():
    '''
    classdocs
    '''

    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
        self.main = None
        self.id = 0
        self.msg = ""
        
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main, msg):
        self.main = main
        self.msg = msg
        return self
    
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caract�re :
    #Exemple : 
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.msg)
    def read(self, main, value):
        self.main = main
        self.id = int(value[1])
        return self
        
    def handle(self):
        self.main.game.clientinattente.append(self.id)
        if (self.main.game.isrunning):
            self.main.sender.publish(self.main.getClient(self.id), PacketInfoGame().init(self.main, "on#"+str(len(self.main.game.clientingame))))
        else:
            for a in self.main.game.clientinattente:
                try:
                    self.main.sender.publish(self.main.getClient(a), PacketInfoGame().init(self.main, "off#"+str(len(self.main.game.clientinattente))))
                except:
                    pass
            if (len(self.main.game.clientinattente) == self.main.MAXPLAYER):
                self.main.game.start()
