#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from .PacketBonus import PacketBonus
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
        return (self.main.protocolmap.getProtocol(self)+"#"+str(self.id)+"#"+str(self.x)+"#"+str(self.y))
    
    def read(self, main, value):
        self.id = value[1]
        self.x = value[2]
        self.y = value[3]
        self.main = main
        return self
        
    def handle(self):
        print(self.main.game.bonus)
        print(str(self.x))
        print(str(self.y))
        print(str(int(int(self.x)/22))+"#"+str(int(int(self.y)/22)))
        if (str(int(int(self.x)/22))+"#"+str(int(int(self.y)/22)) in self.main.game.bonus):
            self.main.game.bonus.remove(str(int(int(self.x)/22))+"#"+str(int(int(self.y)/22)))
            for a in self.main.game.clientingame:
                self.main.sender.publish(self.main.getClient(a), PacketMove().init(self.main, self.id, self.x, self.y))
                self.main.sender.publish(self.main.getClient(a), PacketBonus().init(self.main, "remove", int(int(self.x)/22), int(int(self.y)/22), self.id, random.randint(0, 1)))
        else:   
            for a in self.main.game.clientingame:
                self.main.sender.publish(self.main.getClient(a), PacketMove().init(self.main, self.id, self.x, self.y))
        return self
