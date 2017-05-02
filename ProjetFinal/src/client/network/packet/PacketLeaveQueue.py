'''
Created on 12 fÃ©vr. 2017

@author: mathi
'''
class PacketLeaveQueue():
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

    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.main.id)
