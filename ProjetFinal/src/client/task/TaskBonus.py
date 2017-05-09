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
    def __init__(self, threadID, name, main):
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
        self.x = 0
        self.size = 30.0

# ~ Fonction run de la thread
    def run(self):
        time.sleep(5)
        self.x = len(self.main.game.map[0])*20
        while self.main.running and self.main.ingame:
            if self.bonus0 > -1:
                self.bonus0 += 1
                if self.zone01 is not None:
                    self.main.fenetregame.canvas.delete(self.zone01)
                if self.zone02 is not None:
                    self.main.fenetregame.canvas.delete(self.zone02)
                z = int((float(self.bonus0/30.0))*self.size)

                self.zone01 = self.main.fenetregame.canvas.create_rectangle(self.x-self.size*3, self.bonus0y-3, self.x+3*(z*2-self.size), self.bonus0y+7, fill = "#64FF37", width=0)
                self.zone02 = self.main.fenetregame.canvas.create_rectangle(self.x+3*(z*2-self.size), self.bonus0y-3, self.x+3*(self.size*2-self.size), self.bonus0y+7, fill = "#FF4650", width=0)





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
                for a in self.main.fenetregame.other:
                    if a not in self.main.fenetregame.findlist:
                        self.main.fenetregame.canvas.tag_lower(self.main.fenetregame.other[a][3])

            time.sleep(0.1)
    def startbonus0(self):
        if self.bonus0 == -1:
            self.bonus0y = self.getnbbonus()*22+11
            self.text01 = self.main.writeText(self.x-self.size*3-50, self.bonus0y, "Vision", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone03 = self.main.writeText(self.x-self.size*3, self.bonus0y, "[", self.main.fenetregame.canvas, False, 15, '#D9D526')
            self.zone04 = self.main.writeText(self.x+self.size*3, self.bonus0y, "]", self.main.fenetregame.canvas, False, 15, '#D9D526')
        self.bonus0 = 0
    def getnbbonus(self):
        a = 0
        if self.bonus0 > -1:
            a+=1
        return a
