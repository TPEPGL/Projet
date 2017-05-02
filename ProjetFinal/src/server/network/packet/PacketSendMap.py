#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PacketSendMap():


    def __init__(self):
        self.main = None
        
    def init(self, main):
        self.main = main
        return self
        
    def write(self):
        msg = ""
        for a in self.main.game.map:
            for b in a:
                msg += b
            msg += "_"
        msg = msg[:-1]
        return (self.main.protocolmap.getProtocol(self)+"#"+msg)
