'''
Created on 4 fÃ©vr. 2017

@author: mathi
'''
import threading

from .packet.PacketChat import *
from .packet.PacketConnect import *
from .packet.PacketDisconnect import *
from .packet.PacketInfoGame import *
from .packet.PacketLeaveQueue import *
from .packet.PacketMove import *
from .packet.PacketSendMap import *
from .packet.PacketStartGame import *
from .packet.PacketTest import *
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
            #Boucle infini tant que le programme est lancé
            while(self.main.running):
                try:
                    msg_recu = self.main.connexion_avec_serveur.recv(2048)
                    #Quand le client recoit un méssage du serveur, le programme continue
                    if (msg_recu.decode() != ""):
                        #On décode la méssage : byte -> String
                        msg_recu = self.main.decode(msg_recu.decode())
                        #On découpe le méssage dans une table avec comme séparateur le #
                        # Par exemple "Salut#Coucou#Oui" -> [Salut, Coucou, Oui
                        for a in msg_recu.split("_-_"):
                            if (a != None and a != ''):
                                data = []
                                if ("#" in a):
                                    data = a.split("#")
                                else:
                                    data.append(a)
                                globals()[self.main.protocolmap.getClassName(data[0])]().read(self.main, data).handle()
                           #globals()[self.main.protocolmap.getClassName(data[0])]() -> Permet avec la première information, le protocol de générer une Class du packet correspondant au protocol
                except ConnectionResetError:
                    print("Server Closed")
                    self.main.fenetre.destroy()
