'''
Created on 3 févr. 2017

@author: mathi
'''

#Import
from threading import Timer
from tkinter import *
from tkinter.messagebox import *
import os
import socket
from network.packet.PacketTest import PacketTest
from network.ProtocolMap import ProtocolMap
from network.Receiver import Receiver
from network.Sender import Sender
from network.packet.PacketChat import PacketChat
from network.packet.PacketConnect import PacketConnect
from network.packet.PacketDisconnect import PacketDisconnect
from network.packet.PacketInfoGame import PacketInfoGame
from network.packet.PacketLeaveQueue import PacketLeaveQueue
from network.packet.PacketUpdate import PacketUpdate as PacketUpdate
from network.packet.PacketWin import PacketWin as PacketWin
from task.TaskUpdateConnect import TaskUpdateConnect
from task.TaskAnimation import TaskAnimation
from task.TaskGame2 import TaskGame2
from numpy import append
from FenetreGame import FenetreGame
from Game import Game


if __name__ == '__main__':
    pass

#Class principale
class Main:

    #Initialisation
    def __init__(self):
        #Ip du serveur
        #self.host = '164.132.202.204'
        self.host = 'localhost'
        #Port
        self.port = 12800
        #Initialisation de la connection
        self.connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Valeur de l'id par défault
        self.id = "-1"
        #Initialisation ProtocolMap
        self.protocolmap = ProtocolMap(self)
        #Initialisation Sender
        self.sender = Sender(self)
        #Initialisation taskupdateconnect
        self.taskupdateconnect = None
        #Initialisation Receiver
        self.receiver = Receiver(1, "taskreceiver", self)
        #Initialisation Pseudo
        self.pseudo = ""
        #Initialisation Champ
        self.champ = None
        #Initialisation Fenetre
        self.fenetre = None
        self.fenetregame = None
        #Initialisation Tableau pour le programme
        self.listforfenetre = {"tchatmsg" : [], "sizemini" : False}
        #Initialisation Variable programme en route
        self.running = True
        #Initialisation Définition du chemin d'access
        self.dir = os.getcwd()
        if ("client" not in self.dir):
            self.dir = self.dir+"\\src\\client\\"
        self.tab = -1
        self.menu = "principale"
        self.game = None
        self.taskanim = None
        self.perso = None
        self.touchepref = {"avancer" : "Z", "piege" : "RETURN", "droite" : "D", "gauche" : "Q", "reculer" : "S"}
        self.image = {}
        self.taskpiege = None
        self.taskgame2 = None
        self.taskgame = None
        
        self.ingame = False
         
    def enterkey(self, event):
        if event.keysym == "Return":
            self.verif()
    def onStart(self):
        #Initialisation Création de la fenetre
        self.fenetre = Tk()
        self.fenetre.title("LabyTrap")
        self.fenetre.maxsize(203, 53)
        self.fenetre.minsize(203, 53)
        frame=Frame(self.fenetre, borderwidth=3,relief=GROOVE)
        Label(frame,text="Votre nom : ").grid(row = 0, column = 0)
        self.champ = Entry(frame, bg ='ivory3', fg='maroon')
        self.champ.grid(row = 0, column =1)
        Button(frame,text="Valider",fg='navy', command=self.verif).grid(row = 1, column =1)
        self.fenetre.bind_all("<Key>", self.enterkey)
        frame.pack()
        self.fenetre.mainloop()
        #En attente du remplissable du pseudo
        if (self.pseudo != ""):
            try:
                #Connection avec le serveur
                self.connexion_avec_serveur.connect((self.host, self.port))
                print("Connection au serveur en cours")
                #Reception du méssage + id
                msg_recu = self.connexion_avec_serveur.recv(1024)
                #Décodage du méssage byte -> string
                msg_recu = msg_recu.decode()
                if "connect#" in msg_recu:
                    self.id = msg_recu.split("#")[1]
                    #Au bout de 1s : ça envoie le packetconnect avec le pseudo pour le donner au serveur et confirmer la connection
                    Timer(1.0, lambda : self.sender.publish(PacketConnect().init(self))).start()
                    print("Connect établi, id : ",self.id)
                    #On lance la task TaskupdateConnect (permet de montrer au serveur que l'on est ligne)
                    self.taskupdateconnect = TaskUpdateConnect(0, "taskupdateconnect", self, PacketUpdate)
                    self.taskupdateconnect.start()
                    #Lancement de la task Receiver (permet de recevoir les méssages du serveur)
                    self.receiver.start()
                    #Création de la fenêtre principal
                    self.fenetre = Tk()
                    self.fenetre.title("LabyTrap")
                    
                    #Création du canvas : La ou il y a le jeu
                    self.listforfenetre["canvasgame"] = Canvas(self.fenetre, width=1200, height=500)
                    self.listforfenetre["canvasgame"].pack(side=TOP)
                    
                    
                    self.image["fondprincipale"] = PhotoImage(file = self.dir+'\\image\\Frame avec bouton.png')
                    self.image["PersoMenu"] = PhotoImage(file = self.dir+'\\image\\Perso 1b.png')
                    self.image["Perso2Menu"] = PhotoImage(file = self.dir+'\\image\\Perso 2b.png')
                    self.image["Perso1Jeu"] = PhotoImage(file = self.dir+'\\image\\Perso 1a.png')
                    self.image["Perso2Jeu"] = PhotoImage(file = self.dir+'\\image\\Perso 2a.png')
                    self.image["tchatlogo"] = PhotoImage(file = self.dir+'\\image\\logotchat.png')
                    self.image["fondingame"] = PhotoImage(file = self.dir+'\\image\\Frame avec bouton(dans partie).png')
                    self.image["fondattente"] = PhotoImage(file = self.dir+'\\image\\Frame avec bouton file dattente.png')
                    self.image["fondattente2"] = PhotoImage(file = self.dir+'\\image\\Frame avec bouton(partie en cours).png')
                    self.image["chargement"] = PhotoImage(file = self.dir+'\\image\\chargement.png')
                    self.image["sol"] = PhotoImage(file = self.dir+'\\image\\sol.png')
                    self.image["solsombre"] = PhotoImage(file = self.dir+'\\image\\solsombre.png')
                    self.image["mur"] = PhotoImage(file = self.dir+'\\image\\mur.png')
                    self.image["fond"] = PhotoImage(file = self.dir+'\\image\\tiled-brick.png')
                    self.image["fondgame"] = PhotoImage(file = self.dir+'\\image\\fondgame.png')
                    self.image["bonus"] = PhotoImage(file = self.dir+'\\image\\bonus.png')
                    
                    self.listforfenetre["canvasgame"].create_image(600,250,image=self.image["fond"])
                    self.perso = self.listforfenetre["canvasgame"].create_image(-100,100,image=self.image["PersoMenu"])
                    self.perso2 = self.listforfenetre["canvasgame"].create_image(180,500,image=self.image["Perso2Menu"])
                    self.listforfenetre["canvasgame"].create_image(600,250,image=self.image["fondprincipale"])

                    self.listforfenetre["canvasgame"].create_image(1182,484,image=self.image["tchatlogo"])
                    self.taskanim = TaskAnimation(2, "taskanim", self)
                    self.taskanim.start()
                    self.listforfenetre["canvasgame"].bind("<Button-1>", self.callback)
                    #Création du frame avec le tchat
                    self.listforfenetre["frametchat"] = Frame(self.fenetre, borderwidth=3, relief = GROOVE,width = 1200)
                    self.listforfenetre["scrolltchat"] = Scrollbar(self.listforfenetre["frametchat"])
                    self.listforfenetre["scrolltchat"].pack(side=RIGHT, fill=Y)
                    self.listforfenetre["listtchat"] = Listbox(self.listforfenetre["frametchat"], bd=0, width = 1000, yscrollcommand=self.listforfenetre["scrolltchat"].set)
                    self.listforfenetre["listtchat"].pack()
                    self.listforfenetre["scrolltchat"].config(command=self.listforfenetre["listtchat"].yview)
                    string = StringVar()
                    self.listforfenetre["entrytchat"] = Entry(self.listforfenetre["frametchat"], width = 1200, textvariable=string, bg ='ivory3', fg='maroon')
                    self.listforfenetre["entrytchatstring"] = string
                    self.listforfenetre["entrytchat"].pack()
                    self.listforfenetre["frametchat"].bind_all("<Key>", self.key)
                    self.listforfenetre["frametchat"].pack()  
                    
                    #Taille de la fenetre bloqué
                    self.fenetre.maxsize(1200, 740)
                    self.fenetre.minsize(1200, 740)
                    self.fenetre.mainloop()
                    #Si cette boucle s'arrete -> On dit que le programme est off pour arrêter les task qui sont en route
                    self.running = False
                    self.sender.publish(PacketDisconnect().init(self))
            #Si le serveur est pas en ligne
            except ConnectionRefusedError:
                print("Le serveur n'est pas en ligne")
            #Si on est pas connecté
            except OSError:
                print("vous n'êtes pas connecté !")           
                
    #Appellé quand on clique sur l'écran avec la souris
    def callback(self, event):
        
        if (self.menu == "principale"):
            if (event.x > 470 and event.x < 735 and event.y > 390 and event.y < 450):
                if (askokcancel("Quitter ?", "Etes vous sur de quitter ?")):
                    self.fenetre.destroy()
            if (event.x > 380 and event.x < 806 and event.y > 97 and event.y < 167):
                self.sender.publish(PacketInfoGame().init(self))
        elif (self.menu == "file"):
            if (event.x > 380 and event.x < 800 and event.y > 387 and event.y < 445 ):
                self.menu="principale"
                self.sender.publish(PacketLeaveQueue().init(self))
                self.listforfenetre["canvasgame"].create_image(600,250,image=self.image["fondprincipale"])
                self.listforfenetre["canvasgame"].create_image(1182,484,image=self.image["tchatlogo"])
                
                
                
        if (event.x > 1168 and event.y > 470):
            if (self.listforfenetre["sizemini"] == False):
                self.fenetre.maxsize(1200, 500)
                self.fenetre.minsize(1200, 500)
                self.listforfenetre["sizemini"] = True
            else:
                self.fenetre.maxsize(1200, 690)
                self.fenetre.minsize(1200, 690)
                self.listforfenetre["sizemini"] = False
       
    def writeText(self, x, y, text2, canvas, fond, size, color):
        idtext = None
        if (fond):
            canvas.create_rectangle(x-15, y-20, x+len(text2)*10, y+20, fill = "#009FE3", width=0)
        idtext = canvas.create_text(x, y,text=text2,fill=color,font='Helvetica '+str(size))
        return idtext
    #Appelé quand on appuye sur une touche #Je t'ai configurer les couleurs
    def key(self, event):
        if (event.keysym == "Return" and self.listforfenetre["entrytchat"].get() != ''):
            if (self.listforfenetre["entrytchat"].get() == "/ms"):
                self.sender.publish(PacketTest().init(self))
                self.listforfenetre["entrytchatstring"].set("")
            else:
                self.sender.publish(PacketChat().init(self, self.pseudo+" : "+self.listforfenetre["entrytchat"].get()))
                self.listforfenetre["tchatmsg"].insert(0, self.listforfenetre["entrytchat"].get())
                self.listforfenetre["entrytchatstring"].set("")
        if (event.keysym == "Up"):
            try:
                self.listforfenetre["entrytchatstring"].set(self.listforfenetre["tchatmsg"][self.tab+1])
                self.tab += 1
            except:
                pass
        if (event.keysym == "Down"):
            if (self.tab <= 0):
                self.listforfenetre["entrytchatstring"].set("")
                self.tab = -1
            else:
                self.tab -= 1
                self.listforfenetre["entrytchatstring"].set(self.listforfenetre["tchatmsg"][self.tab])
        
    #Fonction pour rajouter un méssage dans le tchat du client
    def sendMessage(self, msg):
        self.listforfenetre["listtchat"].insert(END, msg)
        self.listforfenetre["listtchat"].yview(END)  

    def startGame(self, value):
        self.ingame = True
        self.sendMessage("Lancement de la partie ...")
        self.fenetregame = FenetreGame(self, value)
        self.game = Game(self)
        self.menu = "game"
        self.listforfenetre["canvasgame"].create_image(600,250,image=self.image["fondingame"])
        self.taskgame2 = TaskGame2(5, "taskgame2", self, PacketWin)
        self.taskgame2.start()
    #Pemet d'encoder les caractères spéciaux car le serveur est en Python 2.7
    def encode(self, value):
        value = value.replace("À", "*%00%").replace("Á", "*%01%").replace("Â", "*%02%").replace("Ã", "*%03%").replace("Ä", "*%04%").replace("Å", "*%05%").replace("Æ", "*%06%").replace("Ç", "*%07%").replace("È", "*%08%").replace("É", "*%09%").replace("Ê", "*%0A%").replace("Ë", "*%0B%").replace("Ì", "*%0C%").replace("Í", "*%0D%").replace("Î", "*%0E%").replace("Ï", "*%0F%")
        value = value.replace("Ð", "*%10%").replace("Ñ", "*%11%").replace("Ò", "*%12%").replace("Ó", "*%13%").replace("Ô", "*%14%").replace("Õ", "*%15%").replace("Ö", "*%16%").replace("Ø", "*%17%").replace("Œ", "*%18%").replace("Š", "*%19%").replace("þ", "*%1A%").replace("Ù", "*%1B%").replace("Ú", "*%1C%").replace("Û", "*%1D%").replace("Ü", "*%1E%").replace("Ý", "*%1F%")
        value = value.replace("Ÿ", "*%20%").replace("à", "*%21%").replace("á", "*%22%").replace("â", "*%23%").replace("ã", "*%24%").replace("ä", "*%25%").replace("å", "*%26%").replace("æ", "*%27%").replace("ç", "*%28%").replace("è", "*%29%").replace("é", "*%2A%").replace("ê", "*%2B%").replace("ë", "*%2C%").replace("ì", "*%2D%").replace("í", "*%2E%").replace("î", "*%2F%")
        value = value.replace("ï", "*%30%").replace("ð", "*%31%").replace("ñ", "*%32%").replace("ò", "*%33%").replace("ó", "*%34%").replace("ô", "*%35%").replace("õ", "*%36%").replace("ö", "*%37%").replace("ø", "*%38%").replace("œ", "*%39%").replace("š", "*%3A%").replace("Þ", "*%3B%").replace("ù", "*%3C%").replace("ú", "*%3D%").replace("û", "*%3E%").replace("ü", "*%3F%")
        value = value.replace("ý", "*%40%").replace("ÿ", "*%41%").replace("¢", "*%42%").replace("ß", "*%43%").replace("¥", "*%44%").replace("£", "*%45%").replace("™", "*%46%").replace("©", "*%47%").replace("®", "*%48%").replace("ª", "*%49%").replace("×", "*%4A%").replace("÷", "*%4B%").replace("±", "*%4C%").replace("²", "*%4D%").replace("³", "*%4E%").replace("¼", "*%4F%")
        value = value.replace("½", "*%50%").replace("¾", "*%51%").replace("µ", "*%52%").replace("¿", "*%53%").replace("¶", "*%54%").replace("·", "*%55%").replace("¸", "*%56%").replace("º", "*%57%").replace("°", "*%58%").replace("¯", "*%59%").replace("§", "*%5A%").replace("…", "*%5B%").replace("¤", "*%5C%").replace("¦", "*%5D%").replace("≠", "*%5E%").replace("¬", '*%5F%')
        value = value.replace("ˆ", "*%60%").replace("¨", "*%61%").replace("‰", "*%62%")
        return value  
             
    #Permet de décoder les caractères spéciaux                                                               
    def decode(self, value):
        value = value.replace("*%00%", "À").replace("*%01%", "Á").replace("*%02%", "Â").replace("*%03%", "Ã").replace("*%04%", "Ä").replace("*%05%", "Å").replace("*%06%", "Æ").replace("*%07%", "Ç").replace("*%08%", "È").replace("*%09%", "É").replace("*%0A%", "Ê").replace("*%0B%", "Ë").replace("*%0C%", "Ì").replace("*%0D%", "Í").replace("*%0E%", "Î").replace("*%0F%", "Ï")
        value = value.replace("*%10%", "Ð").replace("*%11%", "Ñ").replace("*%12%", "Ò").replace("*%13%", "Ó").replace("*%14%", "Ô").replace("*%15%", "Õ").replace("*%16%", "Ö").replace("*%17%", "Ø").replace("*%18%", "Œ").replace("*%19%", "Š").replace("*%1A%", "þ").replace("*%1B%", "Ù").replace("*%1C%", "Ú").replace("*%1D%", "Û").replace("*%1E%", "Ü").replace("*%1F%", "Ý")
        value = value.replace("*%20%", "Ÿ").replace("*%21%", "à").replace("*%22%", "á").replace("*%23%", "â").replace("*%24%", "ã").replace("*%25%", "ä").replace("*%26%", "å").replace("*%27%", "æ").replace("*%28%", "ç").replace("*%29%", "è").replace("*%2A%", "é").replace("*%2B%", "ê").replace("*%2C%", "ë").replace("*%2D%", "ì").replace("*%2E%", "í").replace("*%2F%", "î")
        value = value.replace("*%30%", "ï").replace("*%31%", "ð").replace("*%32%", "ñ").replace("*%33%", "ò").replace("*%34%", "ó").replace("*%35%", "ô").replace("*%36%", "õ").replace("*%37%", "ö").replace("*%38%", "ø").replace("*%39%", "œ").replace("*%3A%", "š").replace("*%3B%", "Þ").replace("*%3C%", "ù").replace("*%3D%", "ú").replace("*%3E%", "û").replace("*%3F%", "ü")
        value = value.replace("*%40%", "ý").replace("*%41%", "ÿ").replace("*%42%", "¢").replace("*%43%", "ß").replace("*%44%", "¥").replace("*%45%", "£").replace("*%46%", "™").replace("*%47%", "©").replace("*%48%", "®").replace("*%49%", "ª").replace("*%4A%", "×").replace("*%4B%", "÷").replace("*%4C%", "±").replace("*%4D%", "²").replace("*%4E%", "³").replace("*%4F%", "¼")
        value = value.replace("*%50%", "½").replace("*%51%", "¾").replace("*%52%", "µ").replace("*%53%", "¿").replace("*%54%", "¶").replace("*%55%", "·").replace("*%56%", "¸").replace("*%57%", "º").replace("*%58%", "°").replace("*%59%", "¯").replace("*%5A%", "§").replace("*%5B%", "…").replace("*%5C%", "¤").replace("*%5D%", "¦").replace("*%5E%", "≠").replace("*%5F%", "¬")
        value = value.replace("*%60%", "ˆ").replace("*%61%", "¨").replace("*%62%", "‰")
        return value     
    
    #Vérifi la longeur du pseudo
    def verif(self):
        if (5 <= len(self.champ.get()) <= 20):
            self.pseudo = self.champ.get()
            self.fenetre.destroy()
        else:
            showwarning("Attention", "votre nom d'utilisateur doit être compris entre 5 et 20 caractères")
            

#Lance le programme
Main().onStart()
