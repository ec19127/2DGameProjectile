import pygame
import math

pygame.init()
def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 1080,900
    window_title = "The Last Samurai"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
create_window()


class ball(object):
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius-1)

    
def ballPath(startx,starty,power,ang,time):
    velx=math.cos(ang)*power
    vely=math.sin(ang)*power
        
    distX=velx*time
    distY=(vely*time)+((-4.9*(time)**2)/2)
    newx=round(distX+startx)
    newy=round(starty-distY)
    return(newx,newy)

def redrawWindow():
    window.fill((64,64,64))
    Projectile.draw(window)
    pygame.draw.line(window,(255,255,255),line[0],line[1])
    
    pygame.display.update()

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

Projectile=ball(300,494,5,(255,255,255))
x=0
y=0
time=0
power=0
angle=0
shoot=False

run=True
while run:

    if shoot:
        if Projectile.y <500 - Projectile.radius:
            time +=0.02
            po=ballPath(x,y,power,angle,time)
            Projectile.x=po[0]
            Projectile.y=po[1]
        else:
            shoot=False
            Projectile.y=494
        
    pos=pygame.mouse.get_pos()
    line=[(Projectile.x,Projectile.y),pos]
    redrawWindow()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if shoot==False:
                shoot=True
                x=Projectile.x
                y=Projectile.y
                time=0
                power=math.sqrt((line[1][1]-line[0][1])**2+(line[1][0]-line[0][0])**2)/8
                angle= findAngle(pos)
        
