#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Timer
import select
import threading


class TaskNewClient(threading.Thread):
    
        #~ Initialisation
        def __init__(self, threadID, name, main, Users):
            threading.Thread.__init__(self)
            self.main = main
            self.Users = Users
            self.threadID = threadID
            self.name = name
            self.id = 1
        
        #~ Fonction run de la thread
        def run(self):
            while(self.main.running):
                connexions_demandees, wlist, xlist = select.select([self.main.connexion_principale],[], [], 0.05)
                verifclient = []
                for connexion in connexions_demandees:
                    connexion_avec_client, infos_connexion = connexion.accept()
                    verifclient.append(connexion_avec_client)
                    message = "connect#"+str(self.id)
                    user = self.Users(connexion_avec_client, self.id)
                    self.main.connectclient.append(user)
                    self.main.taskcheckclient.updateconnect(user)
                    self.id += 1
                    connexion_avec_client.send(message.encode())
