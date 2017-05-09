#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ProtocolMap(object):


    def __init__(self, main):
        self.protocolmap = { "0" : "PacketUpdate", "1" : "PacketTest", "2" : "PacketChat", "3" : "PacketConnect", "4" : "PacketInfoGame", "5" : "PacketLeaveQueue", "6" : "PacketDisconnect", "7" :"PacketStartGame", "8": "PacketSendMap", "9" : "PacketMove", "A" : "PacketWin", "B" : "PacketBonus"}
        self.main = main
        
    def getClassName(self, value):
        return self.protocolmap[value]
    def getProtocol(self, value):
        value = value.__class__.__name__
        for value2 in self.protocolmap:
            if self.protocolmap[value2] == value:
                return value2
        return "-1"
