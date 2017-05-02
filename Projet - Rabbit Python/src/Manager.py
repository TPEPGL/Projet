#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Manager.py
#  
#  Copyright 2017 mathi <mathi@DESKTOP-8107FQB>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#~ Import Rabbit class objet / Day Class / Utils Class
from Day import *
from Utils import *
from Thread import *
#~ Import tkinter
from tkinter import *

try:
	import matplotlib.pyplot as plt
	from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
	from matplotlib.figure import Figure
except ImportError:
	print("Le module matplotlib n'est pas installé !")
	print("Installation des modules en cours :")
	import os
	print("Installing Setuptools...")
	os.system("python -m pip install -U pip setuptools")
	print("Installing MatPlotlib...")
	os.system("python -m pip install matplotlib")
	try:
		import matplotlib.pyplot as plt
		from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
		from matplotlib.figure import Figure
	except ImportError:
		print("Problème lors de l'installation des modules.")
		print("Pour régler ce problème, modifier les lignes 41 et 43 en marquant le chemin d'acces vers Python.")
		sys.exit(0)

#~ Class Orienté object : car 'class Manager:' -> permet d'avoir access à cette partie du code dans les class Rabbit / Day / Utils

restart = 1


class Manager:
	
	
	def __init__(self):

		#~ Tableau des Rabbits
		self.listRabbit = {0 : 2}
		self.listSexeRabbit = {0 : 1}
		self.listGestationRabbit = {0 : {-1 : 1, 0 : 0}}
		
		#~ Class Day -> Initialisation de la Class
		#~ self correspond à la class qui l'appelle -> Permet de récupérer les valeurs uniques de la class Manager -> Principe de l'orienté object -> Class toutes uniques
		self.day = Day(self)
		#~ Initialisation de l'HashMap ( donnée -> valeur ) pour les questions en gros c'est un tableau avec des clé customs -> MaList["lenomdelacasecustom"] = UnTruc 
		self.labelhashmap = {}
		
		#~ Initialisation de la Fenetre Tkinter 
		self.fenetre = Tk()
		
		#~ Initialisation de la HashMap qui contient la Frame ( sous fenêtre qui sera dans la fenêtre principal) qui contiendra les questions
		self.Frame = {1 : Frame(self.fenetre, borderwidth=3,relief=GROOVE)}
		
		#~ Initialisation de la List qui contiendra les Label ( endroit contenant du text qui peut être modifier ou pas par l'utilisateur qui sera dans la Frame[1]
		self.labellist = {}
		
		#~ Initialisation de la Thread (Task faite en parallèle du programme principale, ce qui permet de faire plusieurs action en même temps
		self.thread = None

		#~ Graphique Initialisation
		self.f = Figure(figsize=(5, 4), dpi=100)
		self.ax1 = self.f.add_subplot(111)
		self.canvas = canvas = FigureCanvasTkAgg(self.f, self.fenetre)
		
		
		
	#~ Function Principale lors des questions
	def start(self):
		#Titre de la fenêtre
		self.fenetre.title('Rabbit Compagny - Mathieu / Anthony / David')
		#Couleur de fond
		self.fenetre['bg'] = 'white'
		#Création du Frame dans la fenetre
		self.Frame[1].pack(side=LEFT)
		#Enregistrement des Label dans un tableau pour les récups pour les vérifs
		self.labelhashmap['annee'] = questionFrame(self.Frame[1], "Année de départ : ", 0)
		self.labelhashmap['mois'] = questionFrame(self.Frame[1], "Mois de départ : ", 1)
		self.labelhashmap['minp'] = questionFrame(self.Frame[1], "Minimum de pourcentage de mortalité : ", 2)
		self.labelhashmap['maxp'] = questionFrame(self.Frame[1], "Maximum de poucentage de mortalité : ", 3)
		self.labelhashmap['moimax'] = questionFrame(self.Frame[1], "Nombre de mois : ", 4)
		#Bouton Valider avec comme action, la function verifquestion()
		Button(self.Frame[1],text="Valider",fg='navy', command=self.verifquestion).grid(row = 5, column =0)
		#Lancement de la fenetre
		self.fenetre.mainloop()
		return 2
		
	def verifquestion(self):
		#counter de bonne réponses
		value = 0
		#Condition Is number -> return true si c'est un nombre
		if (is_number(self.labelhashmap['annee'].get()) == True):
			#Fond vert si annee est un nombre
			self.labelhashmap['annee']['bg']= 'lime green'
			value += 1
		else:
			#Sinon rouge
			self.labelhashmap['annee']['bg']= 'firebrick1'
		if (is_number(self.labelhashmap['mois'].get())):
			if (float(self.labelhashmap['mois'].get()) > 0 and float(self.labelhashmap['mois'].get()) < 13):
				self.labelhashmap['mois']['bg']= 'lime green'
				value += 1
			else:
				self.labelhashmap['mois']['bg']= 'firebrick1'
		else:
			self.labelhashmap['mois']['bg']= 'firebrick1'
		if (is_number(self.labelhashmap['minp'].get()) == True):
			if(10 <= float(self.labelhashmap['minp'].get()) <= 30):
				self.labelhashmap['minp']['bg']= 'lime green'
				value += 1
			else:
				self.labelhashmap['minp']['bg']= 'firebrick1'
		else:
			self.labelhashmap['minp']['bg']= 'firebrick1'
		if (is_number(self.labelhashmap['maxp'].get()) == True):
			if (is_number(self.labelhashmap['minp'].get()) == True):
				if(10 <= float(self.labelhashmap['minp'].get()) <= float(self.labelhashmap['maxp'].get()) <= 30):
					self.labelhashmap['maxp']['bg']= 'lime green'
					value += 1
				else:
					self.labelhashmap['maxp']['bg']= 'firebrick1'
			else:
				self.labelhashmap['maxp']['bg']= 'lime green'
		else:
			self.labelhashmap['maxp']['bg']= 'firebrick1'
		if (is_number(self.labelhashmap['moimax'].get()) == True):
			if (float(self.labelhashmap['moimax'].get()) > 0):
				self.labelhashmap['moimax']['bg']= 'lime green'
				value += 1
			else:
				self.labelhashmap['moimax']['bg']= 'firebrick1'
		else:
			self.labelhashmap['moimax']['bg']= 'firebrick1'
		# = 5 si tous est bon
		if (value == 5):
			#Enregistrement des valeurs des questions au lieu de label car on va suprimer le frame
			#Donc les labels seront null après
			self.labelhashmap['annee'] = int(self.labelhashmap['annee'].get())
			self.labelhashmap['mois'] = int(self.labelhashmap['mois'].get())
			self.labelhashmap['minp'] = int(self.labelhashmap['minp'].get())
			self.labelhashmap['maxp'] = int(self.labelhashmap['maxp'].get())
			self.labelhashmap['moimax'] = int(self.labelhashmap['moimax'].get())
			#Destruction du frames avec les question
			self.Frame[1].destroy()
			#Démarrage de la boucle principal pour le lancement de la simulation
			
			#~ Définition de la date de départ
			self.day.setStartDate(self.labelhashmap['mois'], self.labelhashmap['annee'])
			#~ Création d'une nouvelle frame
			#~ Correspond à l'affichage
			self.Frame[1] = Frame(self.fenetre, borderwidth=3,relief=GROOVE, background = 'gray')
			#~ Correspond au bouton
			self.Frame[2] = Frame(self.fenetre, borderwidth=3,relief=GROOVE, width=20, height=20)
			
			#~ Affichage en direct
			string = StringVar()
			Label(self.Frame[1], textvariable=string, width=30).pack()
			self.labellist["femalecount"] = string
			string2 = StringVar()
			Label(self.Frame[1], textvariable=string2, width=30).pack()
			self.labellist["malecount"] = string2
			string4 = StringVar()
			Label(self.Frame[1], textvariable=string4, width=30).pack()
			self.labellist["adultfemale"] = string4
			string3 = StringVar()
			Label(self.Frame[1], textvariable=string3, width=30).pack()
			self.labellist["adultmale"] = string3
			
			#~ Actualise les informations
			self.updateinfo()
		
			#~ Task principale du programme -> Permet de ne pas faire frezze la fenêtre pendant les calculs
			self.thread = myThreadPrincipal(0, "Thread-1", self)
			self.thread.start()
			
			#~ Affichage du graphique
			self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
			self.canvas.show()

			#~ Taille de la fenêtre
			self.fenetre.maxsize(600, 600)
			self.fenetre.minsize(600, 600)
			
			#~ Position des Frame dans la fenêtre
			self.Frame[1].pack(side = LEFT)
			self.Frame[2].pack(side = RIGHT)
			
			#~ Création des boutons avec des fonctions activés différentes
			Button(self.Frame[2], text="Recommencer", command=self.thread.restartfct).pack()
			Button(self.Frame[2], text="Relancer", command=self.restartall).pack()
			Button(self.Frame[2], text="Quitter", command=self.fenetre.destroy).pack()
		
		
	def restartfct(self):
		self.ax1.clear()
		self.canvas.show()
		self.listRabbit = {0 : 2}
		self.listSexeRabbit = {0 : 1}
		self.listGestationRabbit = {0 : {-1 : 1, 0 : 0}}
		self.thread = myThreadPrincipal(0, "Thread-1", self)
		self.thread.start()
		
	def restartall(self):
		global restart
		restart = 1
		self.fenetre.destroy()
		
	def updateinfo(self):
		#~ Change les valeurs à afficher
		self.labellist["malecount"].set("Nombre de mâles : "+str(self.countMale()))
		self.labellist["femalecount"].set("Nombre de female : "+str(self.countFemale()))
		self.labellist["adultmale"].set("Nombre de mâles adultes : "+str(self.countMaleAdult()))
		self.labellist["adultfemale"].set("Nombre de female adultes : "+str(self.countFemaleAdult()))
		
		#~ Si la thread est crée : Update du graphique
		if (self.thread != None):
			x_axis = self.thread.moi
			y_axis = self.countRabbit()
			self.ax1.plot(x_axis, y_axis, 'o')
			self.canvas.show()
			
			
			
	def countRabbit(self):
		count = 0
		for a in range(len(self.listRabbit)):
			count += self.listRabbit[a]
		return count
		
	def countMale(self):
		count = self.countRabbit()
		count -= self.countFemale()
		return count
					
	def countFemale(self):
		count = 0
		for a in range(len(self.listSexeRabbit)):
			count += self.listSexeRabbit[a]
		return count
		
	def countFemaleAdult(self):
		count = 0
		for a in range(len(self.listSexeRabbit)):
			if a > 3:
				count += self.listSexeRabbit[a]
		return count
	
	def countMaleAdult(self):
		count = 0
		for a in range(len(self.listRabbit)):
			if a > 3:
				count += self.listRabbit[a] - self.listSexeRabbit[a]
		return count
		
	

def main():
	#~ variable restart : permet de faire marcher le bouton restart
	global restart
	while restart:
		restart = 0
		#~ Lancement du manager
		manager = Manager()
		manager.start()
	return 1

if __name__ == '__main__':
	main()
