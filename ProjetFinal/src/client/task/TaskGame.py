# coding=utf-8
'''
Created on 5 févr. 2017

@author: mathi
'''
import threading
import time
from tkinter import *


class TaskGame(threading.Thread):
    
        #~ Initialisation
        def __init__(self, threadID, name, main, PacketMove):
            threading.Thread.__init__(self)
            self.main = main
            self.threadID = threadID
            self.name = name
            self.PacketMove = PacketMove
        
        #~ Fonction run de la thread
        def run(self):
            time.sleep(1)
            while(self.main.running and self.main.ingame):
                if (len(self.main.fenetregame.touche) != 0):
                    posy = self.main.fenetregame.posy
                    posx = self.main.fenetregame.posx
                    if self.main.touchepref["piege"] in self.main.fenetregame.touche:
                        self.main.fenetregame.listimage[int((posx)/22)][int((posy)/22)] = PhotoImage(file = self.main.dir+'\\image\\sol.png')
                        self.main.fenetregame.canvas.itemconfig(self.main.fenetregame.listitem[int((posx)/22)][int((posy)/22)], image = self.main.fenetregame.listimage[int((posx)/22)][int((posy)/22)])
                    if self.main.touchepref["avancer"] in self.main.fenetregame.touche:
                        if (self.main.game.map[int((posx-21)/22)][int((posy)/22)] == 0 and self.main.game.map[int((posx-21)/22)][int((posy-11)/22)] == 0):
                            posx -= 11
                    if self.main.touchepref["reculer"] in self.main.fenetregame.touche:
                        if (self.main.game.map[int((posx+21)/22)][int((posy)/22)] == 0 and self.main.game.map[int((posx+21)/22)][int((posy-11)/22)] == 0):
                            posx += 11
                    if self.main.touchepref["droite"] in self.main.fenetregame.touche:
                        if (self.main.game.map[int((posx)/22)][int((posy+21)/22)] == 0 and self.main.game.map[int((posx-11)/22)][int((posy+21)/22)] == 0):
                            posy += 11
                    if self.main.touchepref["gauche"] in self.main.fenetregame.touche:
                        if (self.main.game.map[int((posx)/22)][int((posy-21)/22)] == 0 and self.main.game.map[int((posx-11)/22)][int((posy-21)/22)] == 0):
                            posy -= 11
                    self.main.sender.publish(self.PacketMove().init(self.main, posx, posy))
                time.sleep(0.05)