'''
Created on 4 fÃ©vr. 2017

@author: mathi
'''
import socket


class Sender(object):
    '''
    classdocs
    '''


    def __init__(self, main):
        self.main = main
    
    def publish(self, packet):
        try:
            #Envoie un packet au serveur, le packet va écrire une chaine de caractère de la forme : Protocol(Nombre en fonction du packet) # Information1 # Information2 # ........
            #Cette chaine de carractère va être après transformer en byte grâce à .encode()
            self.main.connexion_avec_serveur.send((self.main.encode(packet.write())+"_-_").encode())
        except socket.error:
            print("Server Closed")
            self.main.fenetre.destroy()
