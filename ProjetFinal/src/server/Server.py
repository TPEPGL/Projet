#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Server.py
#  
#  Copyright 2017 mathi <mathi@DESKTOP-8107FQB>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import socket

from Users import Users as Users
from network.ProtocolMap import ProtocolMap
from network.Receiver import Receiver
from network.Sender import Sender
from network.packet.PacketChat import PacketChat
from task.TaskCheckClient import TaskCheckClient
from task.TaskNewClient import TaskNewClient
from network.packet.PacketInfoGame import PacketInfoGame
from Game import Game

class Main:

    def __init__(self):
        self.hote = ''
        self.port = 12800
        self.tasknewclient = TaskNewClient(1, "tasknew", self, Users)
        self.taskcheckclient = TaskCheckClient(2, "taskcheck", self, PacketInfoGame)
        self.connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectclient = []
        self.receiver = Receiver(3, "taskreceiver", self)
        self.sender = Sender(self)
        self.protocolmap = ProtocolMap(self)
        self.running = True
        self.game = Game(self)
        self.MAXPLAYER = 3

    def onStart(self):
        print("Starting Server")
        self.connexion_principale.bind((self.hote, self.port))
        self.connexion_principale.listen(5)
        print("Port : {}".format(self.port))
        self.tasknewclient.start()
        self.taskcheckclient.start()
        self.receiver.start()
        end = "end"
        msg = ""
        while (msg != end):
            try:
                msg = input()
            except:
                pass
        self.running = False
    
    def getClient(self, value):
        for client in self.connectclient:
            if client.id == value:
                return client
        return None
    
    def getClient2(self, value):
        for client in self.connectclient:
            if client.client == value:
                return client
        return None
        
    def sendMessageTchat(self, msg):
        self.sender.publishall(PacketChat().init(self, msg))
if __name__ == "__main__":
    Main().onStart()

