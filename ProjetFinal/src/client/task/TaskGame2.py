# coding=utf-8
'''
Created on 5 févr. 2017

@author: mathi
'''
import threading
import time
from tkinter import *


class TaskGame2(threading.Thread):
    # ~ Initialisation
    def __init__(self, threadID, name, main, PacketWin):
        threading.Thread.__init__(self)
        self.PacketWin = PacketWin
        self.main = main
        self.threadID = threadID
        self.name = name
        self.personne = None
        self.count = 0
        self.timer = 0
        self.text = None
        self.text2a = None
        self.text2b = None
        self.text3 = None
        self.text4 = None
        self.x = 0
        self.size = 40.0

        # ~ Fonction run de la thread
    def run(self):
        time.sleep(1)
        while (self.main.running and self.main.ingame):
            if (self.timer != -1):
                self.timer += 1
                if (self.text != None):
                    self.main.fenetregame.canvas.delete(self.text)
                t = 60*5-int(self.timer/10)
                tminute = int(t/60)
                tseconde = t-tminute*60
                self.text = self.main.writeText(self.x, 12, str(tminute)+"m "+str(tseconde)+"s", self.main.fenetregame.canvas, False, 15, '#D9D526')
            if (self.timer > 10 * 60 * 5):
                self.main.sender.publish(self.PacketWin().init(self.main, "hider"))
                self.timer = -1
            if (self.count >= 5 * 10):
                self.main.sender.publish(self.PacketWin().init(self.main, "finder"))
                self.count = -1

            if (self.personne in self.main.fenetregame.findlist and self.count != -1):
                self.count += 1
                if (self.text3 != None):
                    self.main.fenetregame.canvas.delete(self.text3)

                if (self.text4 != None):
                    self.main.fenetregame.canvas.delete(self.text4)
                z = int((float(self.count/50.0))*self.size)

                self.text3 = self.main.fenetregame.canvas.create_rectangle(self.x-self.size*3, 50, self.x+3*(z*2-self.size), 60, fill = "#64FF37", width=0)
                self.text4 = self.main.fenetregame.canvas.create_rectangle(self.x+3*(z*2-self.size), 50, self.x+3*(self.size*2-self.size), 60, fill = "#FF4650", width=0)



            elif (len(self.main.fenetregame.findlist) != 0):
                if (self.text2a != None):
                    self.main.fenetregame.canvas.delete(self.text2a)
                if (self.text2b != None):
                    self.main.fenetregame.canvas.delete(self.text2b)

                if (self.text3 != None):
                    self.main.fenetregame.canvas.delete(self.text3)

                if (self.text4 != None):
                    self.main.fenetregame.canvas.delete(self.text4)
                self.count = 0
                self.personne = 0
                for p in range(len(self.main.fenetregame.findlist)):
                    if (self.main.fenetregame.other[self.main.fenetregame.findlist[p]][4] == 1):
                        self.personne = self.main.fenetregame.findlist[p]
                        self.text2a = self.main.writeText(self.x-self.size*3, 52, "[", self.main.fenetregame.canvas, False, 15, '#D9D526')
                        self.text2b = self.main.writeText(self.x+self.size*3, 52, "]", self.main.fenetregame.canvas, False, 15, '#D9D526')
                        break
            else:
                if (self.text2a != None):
                    self.main.fenetregame.canvas.delete(self.text2a)
                if (self.text2b != None):
                    self.main.fenetregame.canvas.delete(self.text2b)

                if (self.text3 != None):
                    self.main.fenetregame.canvas.delete(self.text3)

                if (self.text4 != None):
                    self.main.fenetregame.canvas.delete(self.text4)
                self.count = 0
                self.personne = 0
            time.sleep(0.1)
