import pygame
import math
from Scripts.Colors import *
from Scripts.Globals import *
pygame.init()

class projectile(object):
    def __init__(self,x,y,radius,color,power,time,angle,po,storex,storey):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.power=power
        self.time=time
        self.angle=angle
        self.po=po
        self.storex=storex
        self.storey=storey
        

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius-1)

    def ballPath(self):
        velx=math.cos(self.angle)*self.power
        vely=math.sin(self.angle)*self.power
        
        distX=velx*self.time
        distY=(vely*self.time)+((-9.8*(self.time)**2)/2)
        newx=round(distX+self.storex)
        newy=round(self.storey-distY)
        return(newx,newy)
