'''
Created on 8 févr. 2017

@author: mathi
'''

class PacketChat():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
        self.time = 0
        self.main = None
        self.msg = ""
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main, msg):
        self.main = main
        self.msg = msg
        return self
        
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caract�re :
    #Exemple : 
    #Protocol de la class = 2
    #Message � l'envoyer = "Salut toi"
    
    # -> 2#Salut toi
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.msg)
    
    
    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau d�couper par le s�parateur # recu dans Receiver
    def read(self, main, value):
        self.msg = value[1]
        self.main = main
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le m�ssage dans le tchat
    def handle(self):
        try:
            self.main.sendMessage(self.msg)
        except:
            pass
        #Permet de marquer dans le tchat le m�ssage que l'on a recu
        return self
