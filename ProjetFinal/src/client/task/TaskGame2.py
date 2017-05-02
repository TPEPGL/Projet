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
        self.text2 = None
        self.text3 = None
        self.text4 = None

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
                self.text = self.main.writeText(650, 12, str(tminute)+"m "+str(tseconde)+"s", self.main.fenetregame.canvas, False, 15, '#D9D526')
            if (self.timer > 10 * 60 * 5):
                self.main.sender.publish(self.PacketWin().init(self.main, "hider"))
                self.timer = -1
            if (self.count >= 5 * 10):
                self.main.sender.publish(self.PacketWin().init(self.main, "finder"))
                self.count = -1

            if (self.personne in self.main.fenetregame.findlist and self.count != -1):
                self.count += 1


            elif (len(self.main.fenetregame.findlist) != 0):
                if (self.main.fenetregame.other[self.main.fenetregame.findlist[0]][4] == 1):
                    self.personne = self.main.fenetregame.findlist[0]
                    self.count = 0
                    msg = "["
                    i = 0
                    while i < 20:
                        msg+=" "
                    self.text2 = self.main.writeText(650, 635, msg + "]", self.main.fenetregame.canvas, False, 15, '#D9D526')
                    print(str((self.count/50)*20))
            else:
                if (self.text2 != None):
                    self.main.fenetregame.canvas.delete(self.text2)

                if (self.text3 != None):
                    self.main.fenetregame.canvas.delete(self.text3)

                if (self.text4 != None):
                    self.main.fenetregame.canvas.delete(self.text4)
                self.count = 0
                self.personne = 0
            time.sleep(0.1)