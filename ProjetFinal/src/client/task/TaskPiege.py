# coding=utf-8
'''
Created on 5 févr. 2017

@author: mathi
'''
import threading
import time
from tkinter import *
import random

class TaskPiege(threading.Thread):
    # ~ Initialisation
    def __init__(self, threadID, name, main):
        threading.Thread.__init__(self)
        self.main = main
        self.threadID = threadID
        self.name = name
        self.piege0 = -1
        self.zone01 = None
        self.zone02 = None
        self.zone03 = None
        self.zone04 = None
        self.text01 = None
        self.piege0y = 0
        self.piege1 = -1
        self.zone11 = None
        self.zone12 = None
        self.zone13 = None
        self.zone14 = None
        self.text11 = None
        self.piege1y = 0
        self.x = 0
        self.size = 30.0
        self.id0 = 0

# ~ Fonction run de la thread
    def run(self):
        time.sleep(3)
        self.x = len(self.main.game.map[0])*20
        while self.main.running and self.main.ingame:
            if self.piege0 > -1:
                self.piege0 += 1
                if self.zone01 is not None:
                    self.main.fenetregame.canvas.delete(self.zone01)
                if self.zone02 is not None:
                    self.main.fenetregame.canvas.delete(self.zone02)
                z = int((float(self.piege0/30.0))*self.size)

                self.zone01 = self.main.fenetregame.canvas.create_rectangle(self.x-self.size*3, self.piege0y*22-14, self.x+3*(z*2-self.size), self.piege0y*22-3, fill = "#64FF37", width=0)
                self.zone02 = self.main.fenetregame.canvas.create_rectangle(self.x+3*(z*2-self.size), self.piege0y*22-14, self.x+3*(self.size*2-self.size), self.piege0y*22-3, fill = "#FF4650", width=0)


            if self.piege1 > -1:
                self.piege1 += 1
                if self.zone11 is not None:
                    self.main.fenetregame.canvas.delete(self.zone11)
                if self.zone12 is not None:
                    self.main.fenetregame.canvas.delete(self.zone12)
                z = int((float(self.piege1/50.0))*self.size)

                self.zone11 = self.main.fenetregame.canvas.create_rectangle(self.x-self.size*3, self.piege1y*22-14, self.x+3*(z*2-self.size), self.piege1y*22-3, fill = "#64FF37", width=0)
                self.zone12 = self.main.fenetregame.canvas.create_rectangle(self.x+3*(z*2-self.size), self.piege1y*22-14, self.x+3*(self.size*2-self.size), self.piege1y*22-3, fill = "#FF4650", width=0)



            if self.piege0 > 10*3:
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
                self.piege0 = -1
                self.piege0y = 0
                if self.id0 is not None:
                    self.main.fenetregame.canvas.delete(self.id0)


            if self.piege1 > 10*5:
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
                self.piege1 = -1
                self.piege1y = 0

            time.sleep(0.1)
    def startpiege0(self):
        if self.piege0 == -1:
            self.piege0y = self.getplace()
            self.text01 = self.main.writeText(self.x-self.size*3-100, self.piege0y*22-11, "Obstruction visuelle", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone03 = self.main.writeText(self.x-self.size*3, self.piege0y*22-11, "[", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone04 = self.main.writeText(self.x+self.size*3, self.piege0y*22-11, "]", self.main.fenetregame.canvas, False, 15, '#D9D526')

        if self.id0 is not None:
            self.main.fenetregame.canvas.delete(self.id0)
        self.id0 = self.main.fenetregame.canvas.create_image(self.main.fenetregame.posy, self.main.fenetregame.posx, image=self.main.image["tache"+str(random.randint(1, 3))])

        self.piege0 = 0

    def startpiege1(self):
        if self.piege1 == -1:
            self.piege1y = self.getplace()
            self.text11 = self.main.writeText(self.x-self.size*3-70, self.piege1y*22-11, "Ralentissement", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone13 = self.main.writeText(self.x-self.size*3, self.piege1y*22-11, "[", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone14 = self.main.writeText(self.x+self.size*3, self.piege1y*22-11, "]", self.main.fenetregame.canvas, False, 15, '#D9D526')
        self.piege1 = 0

    def getplace(self):
        a = 0
        b = []
        if self.piege0y > 0:
            b.append(self.piege0y)
        if self.piege1y > 0:
            b.append(self.piege1y)
        if self.main.taskbonus.bonus0y > 0:
            b.append(self.main.taskbonus.bonus0y)
        if self.main.taskbonus.bonus1y > 0:
            b.append(self.main.taskbonus.bonus1y)
        if self.main.taskbonus.bonus2y > 0:
            b.append(self.main.taskbonus.bonus2y)

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
