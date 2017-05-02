#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PacketTest():
    def __init__(self):
        self.id = -1
        self.main = None
        self.time = 0
        
    def init(self, main, id, time):
        self.main = main
        self.id = id
        self.time = time
        return self
        
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+str(self.id)+"#"+str(self.time))
    
    def read(self, main, value):
        self.id = int(value[1])
        self.time = value[2]
        self.main = main
        return self
        
    def handle(self):
        self.main.sender.publish(self.main.getClient(self.id), PacketTest().init(self.main, self.id, self.time))
