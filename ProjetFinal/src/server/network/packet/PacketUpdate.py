#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PacketUpdate():


    def __init__(self):
        self.id = -1
        self.main = None
     
    def read(self, main, value):
        self.id = int(value[1])
        self.main = main
        return self

    
    def handle(self):
        self.main.taskcheckclient.updateconnect(self.main.getClient(self.id))
        return self
