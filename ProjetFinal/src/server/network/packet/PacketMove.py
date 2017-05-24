#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from .PacketBonus import PacketBonus
from .PacketPiege import PacketPiege
class PacketMove():


    def __init__(self):
        self.main = None
        self.x = -1
        self.y = -1
        self.id = -1
        
    def init(self, main, id, x, y):
        self.main = main
        self.x = x
        self.y = y
        self.id = id
        return self
        
    def write(self):
        return self.main.protocolmap.getProtocol(self) + "#" + str(self.id) + "#" + str(self.x) + "#" + str(self.y)
    
    def read(self, main, value):
        self.id = value[1]
        self.x = value[2]
        self.y = value[3]
        self.main = main
        return self
        
    def handle(self):
        bonus = False
        piege = False
        if str(int(int(self.x)/22))+ "#"+str(int(int(self.y)/22)) in self.main.game.piege:
            if self.main.game.piege[str(int(int(self.x)/22))+ "#"+str(int(int(self.y)/22))] != self.id:
                piege = True
                self.main.sender.publish(self.main.getClient(int(self.main.game.piege[str(int(int(self.x)/22))+ "#"+str(int(int(self.y)/22))])), PacketPiege().init(self.main, "remove", int(int(self.x)/22), int(int(self.y)/22), 0))
                del self.main.game.piege[str(int(int(self.x)/22))+"#"+str(int(int(self.y)/22))]
                id2 = random.randint(0, 2)
                if id2 != 2:
                    self.main.sender.publish(self.main.getClient(int(self.id)), PacketPiege().init(self.main, "piege", 0, 0, id2))
                else:
                    find = True
                    while find:
                        self.y = random.randint(0,len(self.main.game.map[0])-1)
                        self.x = random.randint(0,len(self.main.game.map)-1)
                        if self.main.game.map[self.x][self.y] == "0":
                            find = False
                    self.y = 22*self.y+11
                    self.x = 22*self.x+11
        if str(int(int(self.x)/22))+ "#"+str(int(int(self.y)/22)) in self.main.game.bonus:
            self.main.game.bonus.remove(str(int(int(self.x)/22))+"#"+str(int(int(self.y)/22)))
            bonus = True
        for a in self.main.game.clientingame:
            self.main.sender.publish(self.main.getClient(a), PacketMove().init(self.main, self.id, self.x, self.y))
            if bonus:
                self.main.sender.publish(self.main.getClient(a), PacketBonus().init(self.main, "remove", int(int(self.x)/22), int(int(self.y)/22), self.id, random.randint(0, 2)))
        return self
