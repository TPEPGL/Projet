#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket


class Sender(object):
    '''
    classdocs
    '''


    def __init__(self, main):
        self.main = main
    
    def publish(self, user, packet):
        try:
            user.client.send((packet.write()+"_-_").encode())
        except:
            user.client.close()
            print("Un utilisateur s'est disconnecte : "+user.pseudo+" ("+str(user.id)+")")
            self.main.connectclient.remove(user)
            t = Timer(1.0, lambda : self.main.sendMessageTchat("Un utilisateur s'est deconnecte : "+user.pseudo))
            t.start()
    def publishall(self, packet):
        for client in self.main.connectclient:
            try:
                client.client.send((packet.write()+"_-_").encode())
            except socket.error:
                try:
                    client.client.close()
                except NoneType:
                    pass
                print("Un utilisateur s'est disconnecte : "+client.pseudo+" ("+str(client.id)+")")
                self.main.connectclient.remove(client)
                t = Timer(1.0, lambda : self.main.sendMessageTchat("Un utilisateur s'est deconnecte : "+client.pseudo))
                t.start()
                
