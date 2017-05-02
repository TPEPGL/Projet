#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PacketPosePiege():


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
        for a in self.main.game.clientingame:
            self.main.sender.publish(self.main.getClient(a), PacketPosePiege().init(self.main, self.id, self.x, self.y))
        return self
