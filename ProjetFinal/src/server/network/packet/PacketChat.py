#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PacketChat():


    def __init__(self):
        self.time = 0
        self.main = None
        self.msg = ""
        
    def init(self, main, msg):
        self.main = main
        self.msg = msg
        return self
        
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.msg)
    
    def read(self, main, value):
        self.msg = value[1]
        self.main = main
        return self
        
    def handle(self):
        print(self.msg)
        self.main.sender.publishall(PacketChat().init(self.main, self.msg))
        return self
