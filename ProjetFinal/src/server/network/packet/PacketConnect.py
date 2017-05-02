#!/usr/bin/env python
# -*- coding: utf-8 -*-
class PacketConnect():

    def __init__(self):
        self.id = -1
        self.main = None
        self.pseudo = ""
     
    def read(self, main, value):
        self.id = int(value[1])
        self.main = main
        self.pseudo = value[2]
        return self
    
    def init(self, main):
        self.main = main
        return self
        
    def write(self):
        return (self.main.protocolmap.getProtocol(self))
    
    def handle(self):
        isin = False
        for a in self.main.connectclient:
            if (a.pseudo == self.pseudo):
                isin = True
        if (isin == False):
            self.main.sendMessageTchat("Un utilisateur s'est connecte : "+self.pseudo)
            print("Un utilisateur s'est connecte : "+self.pseudo+" ("+str(self.id)+")")
            self.main.getClient(self.id).setPseudo(self.pseudo)
        else:
            self.main.sender.publish(self.main.getClient(self.id), PacketConnect().init(self.main))
        return self
