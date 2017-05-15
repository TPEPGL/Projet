from tkinter import *
from network.packet.PacketMove import PacketMove as PacketMove
from task.TaskGame import TaskGame

class FenetreGame(Toplevel):
    def __init__(self, main, value):
        Toplevel.__init__(self)
        self.main=main
        self.title("LabyTrap")
        self.canvas = Canvas(self, width=1400, height=900, bg = "brown")
        self.image1 = None
        self.Pion = None
        self.canvas.focus_set()
        self.canvas.bind('<KeyPress>', self.pressTouche)
        self.canvas.bind('<KeyRelease>', self.unpressTouche)
        self.canvas.pack(side=TOP)
        self.touche = []
        self.main.taskgame = TaskGame(3, "taskgame", self.main, PacketMove)
        self.main.taskgame.start()
        self.maxsize(10, 10)
        self.minsize(10, 10)
        self.posx = 0
        self.posy = 0
        self.value=value
        self.other =  {}
        self.maptemp = []
        self.listitem = []
        self.findlist = []
        self.role = 0
        self.listpiege = []
        self.invilist = []
        self.bonus2x = 0
        self.bonus2y = 0

    def spawnPion(self, x, y, role):
        if (role == 0):
            self.Pion = self.canvas.create_image(y*22+11,x*22+11,image=self.main.image["Perso2Jeu"])
        else:
            self.Pion = self.canvas.create_image(y*22+11,x*22+11,image=self.main.image["Perso1Jeu"])
        self.posx = x*22+11
        self.posy = y*22+11
        self.role = role
        self.canvas.tag_raise(self.Pion)
    def spawnOtherPion(self, id, x, y, role):
        pion = 0
        if (role == 0):
            pion = self.canvas.create_image(y*22+11,x*22+11,image=self.main.image["Perso2Jeu"])
        else:
            pion = self.canvas.create_image(y*22+11,x*22+11,image=self.main.image["Perso1Jeu"])
        self.other[id] = [x*22+11, y*22+11, self.main.image["Perso2Jeu"], pion, role]
    def pressTouche(self, event):
        if (event.keysym.upper() not in self.touche):
            self.touche.append(event.keysym.upper())
    def unpressTouche(self, event):
        if (event.keysym.upper() in self.touche):
            self.touche.remove(event.keysym.upper())
