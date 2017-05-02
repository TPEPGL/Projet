'''
Created on 12 févr. 2017

@author: mathi
'''
class PacketRole():
    '''
    classdocs
    '''
    
    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
        self.main = None
        self.role = -1
        
    def read(self, main, value):
        self.role = int(value[1])
        self.main = main
        return self
        
    def handle(self):
        if (self.role==0):
            self.main.game.role = "finder"
        elif (self.role==1):
            self.main.game.role = "hider"
        return self
