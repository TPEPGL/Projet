'''
Created on 12 fÃ©vr. 2017

@author: mathi
'''
from tkinter import *
from _tkinter import *
class PacketInfoGame():
    '''
    classdocs
    '''
    
    #Initialisation de la class avec les variables par défault
    def __init__(self):
        self.main = None
        self.infoserver = ""
        self.nbclient  = 0
    
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main):
        self.main = main
        return self

    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.main.id)
    
    def read(self, main, value):
        self.infoserver = value[1]
        self.nbclient = int(value[2])
        self.main = main
        return self
        
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le temps recu dans le tchat en enlever 
    #l'heure en miliseconde de la machine
    #Ce qui nous donnera le temps en miliseconde qui sera le temps pour que le méssage fasse un aller retour
    def handle(self):
        
        if self.infoserver == "off":
            self.main.menu = "file"
            self.main.listforfenetre["canvasgame"].create_image(600,250,image=self.main.image["fondattente"])
            self.main.listforfenetre["canvasgame"].create_image(1182,484,image=self.main.image["tchatlogo"])
            self.main.writeText(610,270, str(self.nbclient), self.main.listforfenetre["canvasgame"], True, 25, '#E94E1B')
        elif self.infoserver == "on":
            self.main.menu = "file"
            self.main.listforfenetre["canvasgame"].create_image(600,250,image=self.main.image["fondattente2"])
            self.main.listforfenetre["canvasgame"].create_image(1182,484,image=self.main.image["tchatlogo"])
            self.main.writeText(610,270, str(self.nbclient), self.main.listforfenetre["canvasgame"], True, 25, '#E94E1B')
        return self
