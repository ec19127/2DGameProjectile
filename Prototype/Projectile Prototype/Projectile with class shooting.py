import pygame
import math

class projectile(object):
    def __init__(self,x,y,radius,color,power,time,angle,po,line,storex,storey):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.power=power
        self.time=time
        self.angle=angle
        self.po=po
        self.line=line
        self.storex=storex
        self.storey=storey
        

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius-1)
    @staticmethod
    def ballPath(startx,starty,power,ang,time):
        velx=math.cos(angle)*power
        vely=math.sin(angle)*power
        
        distX=velx*time
        distY=(vely*time)+((-4.9*(time)**2)/2)
        newx=round(distX+startx)
        newy=round(starty-distY)
        return(newx,newy)

def findAngle(pos):
    sX=Projectile.x
    sY=Projectile.y
    try:
        angle=math.atan((sY-pos[1])/(sX-pos[0]))
    except:
        angle=math.pi/2
    if pos[1]<sY and pos[0] >sX:
        angle=abs(angle)
    elif pos[1] <sY and pos[0] <sX:
        angle=math.pi-angle
    elif pos[1] >sY and pos[0] <sX:
        angle=math.pi+abs(angle)
    elif pos[1] >sY and pos[0] >sX:
        angle=(math.pi *2)-angle
    return angle
