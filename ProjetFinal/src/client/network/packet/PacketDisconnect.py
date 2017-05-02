'''
Created on 12 févr. 2017

@author: mathi
'''
class PacketDisconnect():
    '''
    classdocs
    '''

    def __init__(self):
        self.main = None
    
    def init(self, main):
        self.main = main
        return self
    

    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+str(self.main.id))
