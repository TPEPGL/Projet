#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .PacketInfoGame import PacketInfoGame
class PacketLeaveQueue():

    def __init__(self):
        self.id = -1
        self.main = None
     
    def read(self, main, value):
        self.id = int(value[1])
        self.main = main
        return self

    
    def handle(self):
        self.main.game.clientinattente.remove(self.id)
        if (self.main.game.isrunning):
            pass
        else:
            for a in self.main.game.clientinattente:
                try:
                    self.main.sender.publish(self.main.getClient(a), PacketInfoGame().init(self.main, "off#"+str(len(self.main.game.clientinattente))))
                except:
                    pass
        return self
