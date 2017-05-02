#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Day.py
#  By Means1 - Anthony

class Day:

	#~ Initialisation de la class Day
	def __init__(self, manager):
		self.moihashmap = {"Janvier" : 31, "Février" : 28, "Mars" : 31, "Avril" : 30, "Mai" : 31, "Juin" : 30, "Juillet" : 31, "Aout" : 31, "Septembre" : 30, "Octobre" : 31, "Novembre" : 30, "Décembre" : 31}
		self.moiname = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
		self.datestartmounth = 0
		self.datestartyear = 0
		self.manager = manager
		
	
	#~ Si il y a un jour de chasse
	def getAddPourcent(self, value):
		
		if (value < 3 or value > 7):
			return 10
		else:
			return 0
		
	#~ Donne le moi
	def getMoi(self, nbmoi):
		nbmoi += self.datestartmounth-1
		return nbmoi%12
	#~ Donne l'annee
	def getYear(self, nbmoi):
		nbmoi += self.datestartmounth-1
		return self.datestartyear+(int(nbmoi/12))
		
	#~ Permet de définir une date de départ
	def setStartDate(self, mounth, year):
		self.datestartmounth = mounth
		self.datestartyear = year
		
		
	def getStartDepart(self):
		return "Date de départ : ",self.datestartmounth,":",self.datestartyear



