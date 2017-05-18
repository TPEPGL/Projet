'''
Created on 5 févr. 2017

@author: mathi
'''
import threading
import time



class TaskUpdateConnect(threading.Thread):
    
        #~ Initialisation
        def __init__(self, threadID, name, main, PacketUpdate):
            threading.Thread.__init__(self)
            self.main = main
            self.threadID = threadID
            self.name = name
            self.PacketUpdate = PacketUpdate
        
        #~ Fonction run de la thread
        def run(self):
            #Boucle infini tant que le programme est lanc�
            while self.main.running:
                #Toute les 1 secondes, on envoie le packet Update au serveur
                self.main.sender.publish(self.PacketUpdate().init(self.main))
                time.sleep(1)
