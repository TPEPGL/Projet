#!/usr/bin/env python
# -*- coding: utf-8 -*-
import select
import threading

from .packet.PacketUpdate import *
from .packet.PacketChat import *
from .packet.PacketConnect import *
from .packet.PacketDisconnect import *
from .packet.PacketTest import *
from .packet.PacketInfoGame import *
from .packet.PacketLeaveQueue import *
from .packet.PacketStartGame import *
from .packet.PacketMove import *
from .packet.PacketPosePiege import *
from .packet.PacketWin import *
from .packet.PacketBonus import *

class Receiver(threading.Thread):

        #~ Initialisation
        def __init__(self, threadID, name, main):
            threading.Thread.__init__(self)
            self.main = main
            self.threadID = threadID
            self.name = name

        #~ Fonction run de la thread
        def run(self):
            while(self.main.running):
                clients_a_lire = []
                clientlist = []
                for client in self.main.connectclient:
                    if "[closed]" not in str(client.client):
                        clientlist.append(client.client)
                if (len(clientlist)!=0):
                    try:
                        clients_a_lire, wlist, xlist = select.select(clientlist, [], [], 0.1)
                    except:
                        pass
                    clients_a_lire2 = []
                    for client in clients_a_lire:
                        client2 = self.main.getClient2(client)
                        if (client2 != None):
                            clients_a_lire2.append(client2)
                    for client in clients_a_lire2:
                        msg_recu = ""
                        try:
                            msg_recu = client.client.recv(2048)
                            msg_recu = msg_recu.decode()
                            for a in msg_recu.split("_-_"):
                                if (a != None and a != ''):
                                    data = []
                                    if ("#" in a):
                                        data = a.split("#")
                                    else:
                                        data.append(a)
                                    (globals()[self.main.protocolmap.getClassName(data[0])]()).read(self.main, data).handle()
                        except:
                            pass
