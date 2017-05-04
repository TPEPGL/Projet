#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .PacketInfoGame import PacketInfoGame

class PacketWin():


    def __init__(self):
        self.time = 0
        self.main = None
        self.win = ""

    def init(self, main, msg):
        self.main = main
        self.win = msg
        return self

    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+self.win)

    def read(self, main, value):
        self.win = value[1]
        self.main = main
        return self

    def handle(self):
        if (self.main.game.isrunning):
            for a in self.main.game.clientingame:
                self.main.sender.publish(self.main.getClient(a), PacketWin().init(self.main, self.win))
            self.main.game.stop()
            if (len(self.main.game.clientinattente) < 3):
                for b in self.main.game.clientinattente:
                    self.main.sender.publish(self.main.getClient(b), PacketInfoGame().init(self.main, "off#"+str(len(self.main.game.clientinattente))))
            else:
                self.main.game.start()

        return self
