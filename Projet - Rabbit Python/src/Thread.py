#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Thread.py
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
import threading
import random
import time

class myThreadPrincipal (threading.Thread):
	
		#~ Initialisation
		def __init__(self, threadID, name, manager):
			threading.Thread.__init__(self)
			self.manager = manager
			self.threadID = threadID
			self.name = name
			self.moi = 0
			self.moimax =self.manager.labelhashmap['moimax']
			self.stop = False
		
		#~ Fonction run de la thread
		def run(self):
			print ("Starting " + self.name)
			
			#~ Boucle par moi
			while (self.moimax != self.moi and (self.manager.countRabbit) != 0 and self.stop == False):
				
				#~ Définition de taux de mortalité ce mois ci
				nbrandom = random.randint(self.manager.labelhashmap['minp'],self.manager.labelhashmap['maxp'])
				nbrandom = (nbrandom + self.manager.day.getAddPourcent(self.manager.day.getMoi(self.moi)))/ 100
				
				
				#~ Kill des lapins
				for a in range(len(self.manager.listRabbit)):
					if self.manager.listRabbit[a] != 0:
						nombre = self.manager.listRabbit[a]
						if (a >= 20):
							deathpourcent = nbrandom+((a-20)/20)
						else:
							deathpourcent = nbrandom
						nombre = int((nombre*deathpourcent))
						if (nombre == 0):
							if (random.randint(0, 3*self.manager.listRabbit[a]) == 0):
								nombre += 1
						self.manager.listRabbit[a] -= nombre
						random4 = random.randint(0,nombre)
						if self.manager.listSexeRabbit[a] - random4 > 0:
							self.manager.listSexeRabbit[a] -= random4
						else:
							self.manager.listSexeRabbit[a] = 0
						killrabbit2 = random4
						while killrabbit2 != 0:
							count = 0
							if self.manager.listGestationRabbit[a][-1] - 1 >= 0:
								self.manager.listGestationRabbit[a][-1] -= 1
								killrabbit2 -= 1
							else:
								count += 1
							if self.manager.listGestationRabbit[a][0] -1 >= 0:
								self.manager.listGestationRabbit[a][0] -= 1
								killrabbit2 -= 1
							else:
								count += 1
							if count == 2:
								killrabbit2 = 0
				lenght = len(self.manager.listRabbit)
				newcount = 0
				
				#~ Décalage des lapins dans la case du moi suivant des listes
				for a in range(lenght):
					idr = lenght-a-1

					if self.manager.listRabbit[idr] > 0:
						self.manager.listRabbit[idr + 1] = self.manager.listRabbit[idr]
						self.manager.listSexeRabbit[idr + 1] = self.manager.listSexeRabbit[idr]
						try:
							self.manager.listGestationRabbit[idr+1][0]
						except KeyError:
							self.manager.listGestationRabbit[idr+1] = {-1 : 0, 0 : 0}
							
						if idr > 3:
							self.manager.listGestationRabbit[idr+1][0] = self.manager.listGestationRabbit[idr][-1]
							getgestation = self.manager.listGestationRabbit[idr][0]
							if (getgestation > 0):
								newcount += getgestation
								self.manager.listGestationRabbit[idr+1][-1] = getgestation
						else:
							self.manager.listGestationRabbit[idr+1][-1] = self.manager.listSexeRabbit[idr]
							self.manager.listGestationRabbit[idr+1][0] = 0
					else:
						try:
							self.manager.listRabbit[idr+1] = 0
							self.manager.listSexeRabbit[idr+1] = 0
						except KeyError:
							sertarien = 0
				countnew = 0
				
				#~ Création des nouveaux lapins
				for a in range(newcount):
					nb= random.randint(3,12)
					countnew += nb
					
				#~ Définition des lapins créee dans la case 0
				self.manager.listRabbit[0] = countnew
				self.manager.listSexeRabbit[0] = int(countnew/2)
				self.manager.listGestationRabbit[0] = {-1 : int(countnew/2), 0 : 0}
				self.manager.updateinfo()
				self.moi += 1
				print("Moi ",self.moi, " (",self.manager.day.moiname[self.manager.day.getMoi(self.moi-1)], " ",self.manager.day.getYear(self.moi)," ) : ",self.manager.countRabbit()," Rabbit")
			print ("Exiting " + self.name)
			
		#~ Pour relancer la task
		def restartfct(self):
			if (self.is_alive()):
				self.stop = True
				self.join()
			self.manager.restartfct()
