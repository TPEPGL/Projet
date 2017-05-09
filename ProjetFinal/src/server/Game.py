#!/usr/bin/env python
# -*- coding: utf-8 -*-

from network.packet.PacketStartGame import PacketStartGame
from network.packet.PacketSendMap import PacketSendMap
from network.packet.PacketBonus import PacketBonus
from task.TaskGame import TaskGame
import random
class Game():
    def __init__(self, main):
        self.main = main
        self.isrunning = False
        self.clientingame = []
        self.clientinattente = []
        self.hideplayer = -1
        self.map = []
        self.task = None
        
    def stop(self):
        self.clientingame = []
        self.isrunning = False
        self.hideplayer = -1
        print("Stoped Game")

    def start(self):
         
        print("Starting Game...")
        self.map = []
        nb = random.randint(1,2)
        fichier = open("map"+str(nb)+".txt", "r")
        content = fichier.read().replace("\r", "")
        content = content.split("\n")
        for a in content:
            c = []
            for b in a:
                c.append(b)
            self.map.append(c)
        self.clientingame.append(self.clientinattente[0])
        self.clientingame.append(self.clientinattente[1])
        self.clientingame.append(self.clientinattente[2])
        for d in self.clientingame:
            self.clientinattente.remove(d)
        self.hideplayer = self.clientingame[random.randint(0,self.main.MAXPLAYER-1)]
        msg = str(self.main.MAXPLAYER)
        for a in range(self.main.MAXPLAYER):
            find = True
            while find:
                y = random.randint(0,len(self.map[0])-1)
                x = random.randint(0,len(self.map)-1)
                role = 0
                if (self.hideplayer==self.clientingame[a]):
                    role = 1
                if (self.map[x][y] == "0"):
                    msg += "#"+str(self.clientingame[a])+"#"+str(x)+"#"+str(y)+"#"+str(role)
                    find = False
        for a in self.clientingame:
            self.main.sender.publish(self.main.getClient(a), PacketStartGame().init(self.main, msg)) 
            self.main.sender.publish(self.main.getClient(a), PacketSendMap().init(self.main))
        self.isrunning = True
        self.task = TaskGame(1, "game", self.main, PacketBonus)
        self.task.start()
        print("Started Game... ")
        print(str(self.main.MAXPLAYER) + " Players")
