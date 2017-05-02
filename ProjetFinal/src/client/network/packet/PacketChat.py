'''
Created on 8 fÃ©vr. 2017

@author: mathi
'''

class PacketChat():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par défault
    def __init__(self):
        self.time = 0
        self.main = None
        self.msg = ""
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main, msg):
        self.main = main
        self.msg = msg
        return self
        
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caractère :
    #Exemple : 
    #Protocol de la class = 2
    #Message à l'envoyer = "Salut toi"
    
    # -> 2#Salut toi
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.msg)
    
    
    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau découper par le séparateur # recu dans Receiver
    def read(self, main, value):
        self.msg = value[1]
        self.main = main
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le méssage dans le tchat
    def handle(self):
        self.main.sendMessage(self.msg)
        #Permet de marquer dans le tchat le méssage que l'on a recu
        return self
