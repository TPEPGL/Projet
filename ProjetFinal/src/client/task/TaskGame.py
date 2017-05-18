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
        def __init__(self, threadID, name, main, PacketMove,PacketPiege):
            threading.Thread.__init__(self)
            self.main = main
            self.threadID = threadID
            self.name = name
            self.PacketMove = PacketMove
            self.PacketPiege = PacketPiege
        #~ Fonction run de la thread
        def run(self):
            time.sleep(3)
            while self.main.running and self.main.ingame:
                if len(self.main.fenetregame.touche) != 0:
                    posy = self.main.fenetregame.posy
                    posx = self.main.fenetregame.posx
                    try:
                        if self.main.touchepref["piege"] in self.main.fenetregame.touche and self.main.taskgame2.piege > 0 and self.main.game.map[int(posx / 22)][int(posy / 22)] == 0:
                            id = self.main.fenetregame.listitem[int(posx / 22)][int(posy / 22)]
                            if id not in self.main.fenetregame.listpiege:
                                self.main.fenetregame.canvas.itemconfig(id, image=self.main.image["piege"])
                                self.main.fenetregame.listpiege.append(id)
                                self.main.taskgame2.piege -= 1
                                self.main.sender.publish(self.PacketPiege().init(self.main, int(posx / 22), int(posy / 22),self.main.id))
                        if self.main.touchepref["avancer"] in self.main.fenetregame.touche:
                            if self.main.game.map[int((posx-21)/22)][int(posy /22)] == 0 and self.main.game.map[int((posx-21)/22)][int((posy-11)/22)] == 0 or self.main.taskbonus.bonus2 != -1 and self.main.game.map[int((posx-21)/22)][int((posy)/22)] != 2 and self.main.game.map[int((posx-21)/22)][int((posy-11)/22)] != 2:
                                posx -= 11
                        if self.main.touchepref["reculer"] in self.main.fenetregame.touche:
                            if self.main.game.map[int((posx+21)/22)][int(posy /22)] == 0 and self.main.game.map[int((posx+21)/22)][int((posy-11)/22)] == 0 or self.main.taskbonus.bonus2 != -1 and self.main.game.map[int((posx+21)/22)][int((posy)/22)] != 2 and self.main.game.map[int((posx+21)/22)][int((posy-11)/22)] != 2:
                                posx += 11
                        if self.main.touchepref["droite"] in self.main.fenetregame.touche:
                            if self.main.game.map[int(posx /22)][int((posy+21)/22)] == 0 and self.main.game.map[int((posx-11)/22)][int((posy+21)/22)] == 0 or self.main.taskbonus.bonus2 != -1 and self.main.game.map[int((posx)/22)][int((posy+21)/22)] != 2 and self.main.game.map[int((posx-11)/22)][int((posy+21)/22)] != 2:
                                posy += 11
                        if self.main.touchepref["gauche"] in self.main.fenetregame.touche:
                            if self.main.game.map[int(posx /22)][int((posy-21)/22)] == 0 and self.main.game.map[int((posx-11)/22)][int((posy-21)/22)] == 0 or self.main.taskbonus.bonus2 != -1 and self.main.game.map[int((posx)/22)][int((posy-21)/22)] != 2 and self.main.game.map[int((posx-11)/22)][int((posy-21)/22)] != 2:
                                posy -= 11
                        if self.main.fenetregame.posy != posy or self.main.fenetregame.posx != posx:
                            self.main.sender.publish(self.PacketMove().init(self.main, posx, posy))
                    except IndexError:
                        print("error")
                time.sleep(0.05)
