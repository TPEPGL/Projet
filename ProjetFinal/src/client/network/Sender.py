'''
Created on 4 févr. 2017

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
            #Envoie un packet au serveur, le packet va �crire une chaine de caract�re de la forme : Protocol(Nombre en fonction du packet) # Information1 # Information2 # ........
            #Cette chaine de carract�re va �tre apr�s transformer en byte gr�ce � .encode()
            self.main.connexion_avec_serveur.send((self.main.encode(packet.write())+"_-_").encode())
        except socket.error:
            print("Server Closed")
            self.main.fenetre.destroy()
