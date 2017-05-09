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

# ~ Fonction run de la thread
    def run(self):
        time.sleep(1)
        while self.main.running and self.main.ingame:
            if self.bonus0 > -1:
                self.bonus0 += 1
            if self.bonus0 > 10*3:
                self.bonus0 = -1
                for a in self.main.fenetregame.other:
                    if a not in self.main.fenetregame.findlist:
                        self.main.fenetregame.canvas.tag_lower(self.main.fenetregame.other[a][3])
            time.sleep(0.1)
