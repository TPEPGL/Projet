'''
Created on 8 fÃ©vr. 2017

@author: mathi
'''

import time

class PacketWin():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par défault
    def __init__(self):
        self.time = 0
        self.main = None
        self.win = ""
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main, win):
        self.main = main
        self.win = win
        return self
        
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caractère :
    #Exemple : 
    #Protocol de la class = 2
    #Message à l'envoyer = "Salut toi"
    
    # -> 2#Salut toi
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.win)
    
    
    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau découper par le séparateur # recu dans Receiver
    def read(self, main, value):
        self.win = value[1]
        self.main = main
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le méssage dans le tchat
    def handle(self):
        role = 0
        if (self.win == "hider"):
            role = 1
        if (self.main.fenetregame.role == role):
            self.main.writeText(610,270, "Vous avez gagne !", self.main.fenetregame.canvas, False, 60)
        else:
            self.main.writeText(610,270, "Vous avez perdu !", self.main.fenetregame.canvas, False, 60)
        time.sleep(5)
        self.main.fenetregame.destroy()
        self.main.game = None
        self.main.fenetregame = None
        self.main.menu = "principale"
        self.main.listforfenetre["canvasgame"].create_image(600,250,image=self.main.image["fondprincipale"])
        self.main.ingame = False
        return self
