'''
Created on 4 févr. 2017

@author: mathi
'''

class ProtocolMap(object):


    def __init__(self, main):
        #On enregistrer les protocol en les associant avec le nom d'une class
        self.protocolmap = { "0" : "PacketUpdate", "1" : "PacketTest", "2" : "PacketChat", "3" : "PacketConnect", "4" : "PacketInfoGame", "5" : "PacketLeaveQueue", "6" : "PacketDisconnect", "7" :"PacketStartGame", "8": "PacketSendMap", "9" : "PacketMove", "A" : "PacketWin"}
        self.main = main
        
        
        #On rentre le protocol et on revoit le nom de la class, par exemple : On veut le nom de la class avec le protocol 2 et on recoit PacketChat
    def getClassName(self, value):
        return self.protocolmap[value]
    
    
        #On rentre le nom de la class et on recoit le protocol, par exemple: On veut le protocol de la class PacketChat -> on recoit 2
    def getProtocol(self, value):
        value = type(value).__name__
        for value2 in self.protocolmap:
            if self.protocolmap[value2] == value:
                return value2
        return -1
