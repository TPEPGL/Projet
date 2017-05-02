#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Utils.py
#  By Means1


from tkinter import *


#~ Fonction pour afficher un endroit pour répondre à une question
def questionFrame(frame, title, rowvalue):
	#~ Initialisation de l'endroit
	Label(frame,text=title).grid(row = rowvalue, column = 0)
	#~ Value qui va être modifier par l'user
	annee = StringVar()
	#~ Initialisation du champ pour écrire
	champ = Entry(frame, textvariable=annee, bg ='ivory3', fg='maroon')
	#~ Mise en place du champ dans la frame
	champ.grid(row = rowvalue, column =1)
	#~ Retourne le champ
	return champ
	
#~ Fonction pour voir si c'est un nombre
def is_number(s):
	#~ Permet d'éxécuter un code et si il y a une erreur, ça lance le except
    try:
		#~ Si c'est pas un nombre -> erreur
        float(s)
    except ValueError:
        try:
			#~ Si c'est pas un complexe -> Erreur
            complex(s)
        except ValueError:
            return False

    return True
