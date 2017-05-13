#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Timer
import threading
import time
import random

class TaskGame(threading.Thread):
    
        #~ Initialisation
        def __init__(self, threadID, name, main, PacketBonus):
            threading.Thread.__init__(self)
            self.main = main
            self.threadID = threadID
            self.name = name
            self.PacketBonus = PacketBonus
        #~ Fonction run de la thread
        def run(self):
            time.sleep(10)
            while self.main.game.isrunning:
                
                find = True
                y = 0
                x = 0
                while find:
                    y = random.randint(0,len(self.main.game.map[0])-1)
                    x = random.randint(0,len(self.main.game.map)-1)
                    if self.main.game.map[x][y] == "0":
                        find = False
                self.main.game.bonus.append(str(x)+"#"+str(y))
                for a in self.main.game.clientingame:
                    self.main.sender.publish(self.main.getClient(a), self.PacketBonus().init(self.main, "pose", x, y, 0, 0)) 
                
                time.sleep(random.randint(15,30))
                
      
