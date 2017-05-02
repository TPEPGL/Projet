#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Timer
import threading
import time


class TaskCheckClient(threading.Thread):
    
        #~ Initialisation
        def __init__(self, threadID, name, main, packetInfo):
            threading.Thread.__init__(self)
            self.main = main
            self.threadID = threadID
            self.name = name
            self.packetInfo = packetInfo
            self.verif = []
        
        #~ Fonction run de la thread
        def run(self):
            while(self.main.running):
                time.sleep(4)
                stopclient = []
                for client in self.main.connectclient:
                    if client not in self.verif:
                        stopclient.append(client)
                for client in stopclient:
                    self.removeClient(client)
                self.verif = []
                
        def updateconnect(self, value):
            self.verif.append(value)
            
        def removeClient(self, client):
            client.client.close()
            print("Un utilisateur s'est disconnecte : "+client.pseudo+" ("+str(client.id)+")")
            self.main.connectclient.remove(client)
            if (client.pseudo != ""):
                t = Timer(1.0, lambda : self.main.sendMessageTchat("Un utilisateur s'est deconnecte : "+client.pseudo))
                t.start()
            if (client.id in self.main.game.clientinattente):
                self.main.game.clientinattente.remove(client.id)
                for a in self.main.game.clientinattente:
                    try:
                        self.main.sender.publish(self.main.getClient(a),  self.packetInfo().init(self.main, "off#"+str(len(self.main.game.clientinattente))))
                    except:
                        pass