'''
Created on 8 févr. 2017

@author: mathi
'''

from tkinter import *
class PacketSendMap():
    '''
    classdocs
    '''
    #Initialisation de la class avec les variables par d�fault
    def __init__(self):
        self.map = []
        self.main = None
        
    #Fonction utiliser pour RECEVOIR: Permet d'inition les variables avec le tableau d�couper par le s�parateur # recu dans Receiver
    def read(self, main, value):
        self.msg = value[1]
        self.msg = self.msg.split("_")
        for a in self.msg:
            c = []
            for b in a:
                c.append(int(b))
            self.map.append(c)
        self.main = main
        return self
        
    #Fonction utiliser pour RECEVOIR : Va effectuer une action quand on recoit le packet, ici on va marquer le m�ssage dans le tchat
    def handle(self):
        self.main.game.map = self.map
        sizex = len(self.map)*22
        sizey = len(self.map[0])*22
        x = 0
        t = self.main.fenetregame.canvas.create_image(110,45,image=self.main.image["chargement"])
        self.main.fenetregame.maxsize(220, 90)
        self.main.fenetregame.minsize(220, 90)
        listitem =[]
        for a in self.map:
            y = 0
            list2=[]
            for b in a:
                if (b == 0):
                    temp = self.main.fenetregame.canvas.create_image(y+11,x+11,image=self.main.image["solsombre"])
                    self.main.fenetregame.canvas.tag_lower(temp)
                    list2.append(temp)
                elif (b == 1):
                    temp = self.main.fenetregame.canvas.create_image(y+11,x+11,image=self.main.image["mur"])
                    self.main.fenetregame.canvas.tag_lower(temp)
                    list2.append(temp)
                else:
                    list2.append("")
                y += 22
            x += 22
            listitem.append(list2)
        self.main.fenetregame.listitem = listitem
        nbjoueur = int(self.main.fenetregame.value[1])
        for a in range(nbjoueur):
            if (self.main.fenetregame.value[4*a+2]== self.main.id):
                self.main.fenetregame.spawnPion(int(self.main.fenetregame.value[4*a+3]), int(self.main.fenetregame.value[4*a+4]), int(self.main.fenetregame.value[4*a+5]))
            else:
                self.main.fenetregame.spawnOtherPion(int(self.main.fenetregame.value[4*a+2]), int(self.main.fenetregame.value[4*a+3]), int(self.main.fenetregame.value[4*a+4]), int(self.main.fenetregame.value[4*a+5]))
        self.main.fenetregame.maxsize(sizey, sizex)
        self.main.fenetregame.minsize(sizey, sizex)
        self.main.fenetregame.canvas.delete(t)
        self.x = self.main.fenetregame.posx
        self.y = self.main.fenetregame.posy
        map = []
        map.append(self.main.fenetregame.listitem[int(self.x / 22)][int(self.y / 22)])
            
        if (self.main.game.map[int((self.x + 22) / 22)][int(self.y / 22)] == 0):
            map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int(self.y / 22)])
            if (self.main.game.map[int((self.x + 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int((self.y + 22) / 22)])
            if (self.main.game.map[int((self.x + 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int((self.y - 22) / 22)])
            if (self.main.game.map[int((self.x + 44) / 22)][int(self.y / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int((self.x + 44) / 22)][int((self.y) / 22)])
                if (self.main.game.map[int((self.x + 66) / 22)][int(self.y / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x + 66) / 22)][int((self.y) / 22)])
                if (self.main.game.map[int((self.x + 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int((self.x + 44) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x + 44) / 22)][int((self.y - 22) / 22)]) 
                if (self.main.game.map[int((self.x + 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int((self.x + 44) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x + 44) / 22)][int((self.y + 22) / 22)])                                       
        if (self.main.game.map[int((self.x - 22) / 22)][int(self.y / 22)] == 0):
            map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int(self.y / 22)])
            if (self.main.game.map[int((self.x - 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int((self.y + 22) / 22)])
            if (self.main.game.map[int((self.x - 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int((self.y - 22) / 22)])
            if (self.main.game.map[int((self.x - 44) / 22)][int(self.y / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int((self.x - 44) / 22)][int(self.y / 22)]) 
                if (self.main.game.map[int((self.x - 66) / 22)][int(self.y / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x - 66) / 22)][int(self.y / 22)]) 
                if (self.main.game.map[int((self.x - 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int((self.x - 44) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x - 44) / 22)][int((self.y - 22) / 22)]) 
                if (self.main.game.map[int((self.x - 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int((self.x - 44) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x - 44) / 22)][int((self.y + 22) / 22)])                 
        if (self.main.game.map[int(self.x / 22)][int((self.y + 22) / 22)] == 0):
            map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y + 22) / 22)])
            if (self.main.game.map[int(self.x / 22)][int((self.y + 44) / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y + 44) / 22)])
                if (self.main.game.map[int(self.x / 22)][int((self.y + 66) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y + 66) / 22)])
                if (self.main.game.map[int((self.x - 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int((self.x - 22) / 22)][int((self.y + 44) / 22)] == 0 and self.main.game.map[int((self.x-22) / 22)][int((self.y) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int((self.y + 44) / 22)])
                if (self.main.game.map[int((self.x + 22) / 22)][int((self.y + 22) / 22)] == 0 and self.main.game.map[int((self.x + 22) / 22)][int((self.y + 44) / 22)] == 0 and self.main.game.map[int((self.x+22) / 22)][int((self.y) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int((self.y + 44) / 22)])  
        if (self.main.game.map[int(self.x / 22)][int((self.y - 22) / 22)] == 0):
            map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y - 22) / 22)])
            if (self.main.game.map[int(self.x / 22)][int((self.y - 44) / 22)] == 0):
                map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y - 44) / 22)])
                if (self.main.game.map[int(self.x / 22)][int((self.y - 66) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int(self.x / 22)][int((self.y - 66) / 22)])
                if (self.main.game.map[int((self.x - 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int((self.x - 22) / 22)][int((self.y - 44) / 22)] == 0 and self.main.game.map[int((self.x-22) / 22)][int((self.y) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x - 22) / 22)][int((self.y - 44) / 22)])
                if (self.main.game.map[int((self.x + 22) / 22)][int((self.y - 22) / 22)] == 0 and self.main.game.map[int((self.x + 22) / 22)][int((self.y - 44) / 22)] == 0 and self.main.game.map[int((self.x+22) / 22)][int((self.y) / 22)] == 0):
                    map.append(self.main.fenetregame.listitem[int((self.x + 22) / 22)][int((self.y - 44) / 22)])                
        for a in self.main.fenetregame.maptemp:
            if (a not in map):
                self.main.fenetregame.canvas.itemconfig(a, image=self.main.image["solsombre"])
        for b in map:
            self.main.fenetregame.canvas.itemconfig(b, image=self.main.image["sol"])
        self.main.fenetregame.maptemp = map
        self.main.taskgame2.x = len(self.main.game.map[0])*22/2
        self.main.fenetregame.canvas.tag_lower(self.main.fenetregame.canvas.create_image(len(self.main.game.map[0])*22/2, len(self.main.game.map)*22/2,image=self.main.image["fondgame"]))

        for b in self.main.fenetregame.other:
            if (self.main.fenetregame.listitem[int((self.map[b][0]) / 22)][int((self.main.fenetregame.other[b][1]) / 22)] in self.main.fenetregame.maptemp):
                self.main.fenetregame.canvas.tag_raise(self.main.fenetregame.other[b][3])
                if b not in self.main.fenetregame.findlist:
                    self.main.fenetregame.findlist.append(b)
            else:
                self.main.fenetregame.canvas.tag_lower(self.main.fenetregame.other[b][3])
                if b in self.main.fenetregame.findlist:
                    self.main.fenetregame.findlist.remove(b)
        return self
