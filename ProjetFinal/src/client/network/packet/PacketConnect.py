'''
Created on 12 fÃ©vr. 2017

@author: mathi
'''
class PacketConnect():
    '''
    classdocs
    '''

    #Initialisation de la class avec les variables par défault
    def __init__(self):
        self.main = None
    
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main):
        self.main = main
        return self
    
    
    def read(self, main, value):
        self.main = main
        return self
        
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le temps recu dans le tchat en enlever 
    #l'heure en miliseconde de la machine
    #Ce qui nous donnera le temps en miliseconde qui sera le temps pour que le méssage fasse un aller retour
    def handle(self):
        print("Pseudo deja utilise")
        self.main.fenetre.destroy()
        return self
    
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caractère :
    #Exemple : 
    #Id du joueur = 23
    #Protocol de la class = 3
    #Pseudo = "Coulaki"
    
    # -> 3#23#Coulaki
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+str(self.main.id)+"#"+self.main.pseudo)
