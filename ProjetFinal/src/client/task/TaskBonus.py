# coding=utf-8
'''
Created on 5 févr. 2017

@author: mathi
'''
import threading
import time
from tkinter import *


class TaskBonus(threading.Thread):
    # ~ Initialisation
    def __init__(self, threadID, name, main, PacketBonus):
        threading.Thread.__init__(self)
        self.main = main
        self.threadID = threadID
        self.name = name
        self.bonus0 = -1
        self.zone01 = None
        self.zone02 = None
        self.zone03 = None
        self.zone04 = None
        self.text01 = None
        self.bonus0y = 0
        self.bonus1 = -1
        self.zone11 = None
        self.zone12 = None
        self.zone13 = None
        self.zone14 = None
        self.text11 = None
        self.bonus1y = 0
        self.x = 0
        self.size = 30.0
        self.PacketBonus = PacketBonus

# ~ Fonction run de la thread
    def run(self):
        time.sleep(5)
        self.x = len(self.main.game.map[0])*20
        while self.main.running and self.main.ingame:
            print(self.main.fenetregame.invilist)
            if self.bonus0 > -1:
                self.bonus0 += 1
                if self.zone01 is not None:
                    self.main.fenetregame.canvas.delete(self.zone01)
                if self.zone02 is not None:
                    self.main.fenetregame.canvas.delete(self.zone02)
                z = int((float(self.bonus0/30.0))*self.size)

                self.zone01 = self.main.fenetregame.canvas.create_rectangle(self.x-self.size*3, self.bonus0y*22-14, self.x+3*(z*2-self.size), self.bonus0y*22-3, fill = "#64FF37", width=0)
                self.zone02 = self.main.fenetregame.canvas.create_rectangle(self.x+3*(z*2-self.size), self.bonus0y*22-14, self.x+3*(self.size*2-self.size), self.bonus0y*22-3, fill = "#FF4650", width=0)


            if self.bonus1 > -1:
                self.bonus1 += 1
                if self.zone11 is not None:
                    self.main.fenetregame.canvas.delete(self.zone11)
                if self.zone12 is not None:
                    self.main.fenetregame.canvas.delete(self.zone12)
                z = int((float(self.bonus1/50.0))*self.size)

                self.zone11 = self.main.fenetregame.canvas.create_rectangle(self.x-self.size*3, self.bonus1y*22-14, self.x+3*(z*2-self.size), self.bonus1y*22-3, fill = "#64FF37", width=0)
                self.zone12 = self.main.fenetregame.canvas.create_rectangle(self.x+3*(z*2-self.size), self.bonus1y*22-14, self.x+3*(self.size*2-self.size), self.bonus1y*22-3, fill = "#FF4650", width=0)





            if self.bonus0 > 10*3:
                if self.zone03 is not None:
                    self.main.fenetregame.canvas.delete(self.zone03)
                if self.zone04 is not None:
                    self.main.fenetregame.canvas.delete(self.zone04)
                if self.zone01 is not None:
                    self.main.fenetregame.canvas.delete(self.zone01)
                if self.zone02 is not None:
                    self.main.fenetregame.canvas.delete(self.zone02)
                if self.text01 is not None:
                    self.main.fenetregame.canvas.delete(self.text01)
                self.bonus0 = -1
                self.bonus0y = 0
                for a in self.main.fenetregame.other:
                    if a not in self.main.fenetregame.findlist:
                        self.main.fenetregame.canvas.tag_lower(self.main.fenetregame.other[a][3])

            if self.bonus1 > 10*5:
                if self.zone13 is not None:
                    self.main.fenetregame.canvas.delete(self.zone13)
                if self.zone14 is not None:
                    self.main.fenetregame.canvas.delete(self.zone14)
                if self.zone11 is not None:
                    self.main.fenetregame.canvas.delete(self.zone11)
                if self.zone12 is not None:
                    self.main.fenetregame.canvas.delete(self.zone12)
                if self.text11 is not None:
                    self.main.fenetregame.canvas.delete(self.text11)
                self.bonus1 = -1
                self.bonus1y = 0
                self.main.sender.publish(self.PacketBonus().init(self.main, "bonus1", 0, 0, int(self.main.id), 0))
            time.sleep(0.1)
    def startbonus0(self):
        if self.bonus0 == -1:
            self.bonus0y = self.getplace()
            self.text01 = self.main.writeText(self.x-self.size*3-50, self.bonus0y*22-11, "Vision", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone03 = self.main.writeText(self.x-self.size*3, self.bonus0y*22-11, "[", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone04 = self.main.writeText(self.x+self.size*3, self.bonus0y*22-11, "]", self.main.fenetregame.canvas, False, 15, '#D9D526')
            for a in self.main.fenetregame.other:
                self.main.fenetregame.canvas.tag_raise(self.main.fenetregame.other[a][3])
        self.bonus0 = 0

    def startbonus1(self):
        if self.bonus1 == -1:
            self.bonus1y = self.getplace()
            self.text11 = self.main.writeText(self.x-self.size*3-70, self.bonus1y*22-11, "Invisibilité", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone13 = self.main.writeText(self.x-self.size*3, self.bonus1y*22-11, "[", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone14 = self.main.writeText(self.x+self.size*3, self.bonus1y*22-11, "]", self.main.fenetregame.canvas, False, 15, '#D9D526')
        self.bonus1 = 0
    def getplace(self):
        a = 0
        b = []
        if self.bonus0y > 0:
            b.append(self.bonus0y)
        if self.bonus1y > 0:
            b.append(self.bonus1y)
        d = 0
        for c in range(2):
            if c+1 not in b:
                a = c+1
                break
            else:
                if c+1 > d:
                    d = c+1
        if a == 0:
            return d+1
        else:
            return a
