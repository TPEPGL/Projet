#!/usr/bin/env python
# -*- coding: utf-8 -*-
class PacketRole():
    '''
    classdocs
    '''

    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
        self.main = None
        self.role = -1
        
        
    #Fonction utiliser pour ENVOYER : Permet d'initier les variables
    def init(self, main, role):
        self.main = main
        self.role = role
        return self
    
    #Fonction utiliser pour ENVOYER : Permet de transformer les informations de la class en une chaine de caract�re :
    #Exemple : 
    def write(self):
        return (self.main.protocolmap.getProtocol(self)+"#"+str(self.role))
