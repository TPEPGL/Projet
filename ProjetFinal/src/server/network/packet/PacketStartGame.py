#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
class PacketStartGame():


    def __init__(self):
        self.main = None
        self.msg = ""
    def init(self, main, msg):
        self.main = main
        self.msg = msg
        return self
        
    def write(self):
			
        return (self.main.protocolmap.getProtocol(self)+"#"+self.msg)
