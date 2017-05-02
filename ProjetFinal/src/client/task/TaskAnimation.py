'''
Created on 5 févr. 2017

@author: mathi
'''
import threading
import time
class TaskAnimation(threading.Thread):
    
        #~ Initialisation
        def __init__(self, threadID, name, main):
            threading.Thread.__init__(self)
            self.main = main
            self.threadID = threadID
            self.name = name
            self.x = -200
            self.y = 500
            self.a = True
            self.b = True
        
        #~ Fonction run de la thread
        def run(self):
            while(self.main.running):
                time.sleep(0.1)
                if (self.x == 1280):
                    self.a = False
                if (self.x == -100):
                    self.a = True
               
                
                if (self.y == 600):
                    self.b = False
                    
                if (self.y == 500):
                    self.b = True
                
              
                if (self.a):
                    self.main.listforfenetre["canvasgame"].move(self.main.perso,20,0)
                    self.x += 20
                else:
                    self.main.listforfenetre["canvasgame"].move(self.main.perso,-20,0)
                    self.x -= 20
				
                if (self.b):
                    self.main.listforfenetre["canvasgame"].move(self.main.perso2,0,10)
                    self.y += 10
				
                else:
                    self.main.listforfenetre["canvasgame"].move(self.main.perso2,0,-10)
                    self.y -= 10			
