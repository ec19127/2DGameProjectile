import pygame
import math
from Scripts.utilities import *
from Scripts.Colors import *
from Scripts.Spell import *
from Scripts.Globals import *
from Scripts.MapGenerator import *
pygame.init()
def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 1080,900
    window_title = "The Last Samurai"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
create_window()
#Images
PlayerC=pygame.image.load("Graphics\MAIN.png")

#Mesurements
Tilesize=64
Size_x=32
Size_y=32
#Player coordinates
Player_x=0
Player_y=Tilesize*3+Size_y
#Player Movements Logic
Vel=1
JVel=2
DVel=100
PlayerMove=0
countJumps=0
countDash=0
countlimit=0
#Projectile
bullets=[]
def findAngle(pos,storex,storey):
    sX=storex
    sY=storey
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
def TrajectoryPath(cangle,cpower,ctime,scx,scy):
    velx=math.cos(cangle)*cpower
    vely=math.sin(cangle)*cpower
        
    distX=velx*ctime
    distY=(vely*ctime)+((-9.8*(ctime)**2)/2)
    newx=round(distX+scx)
    newy=round(scy-distY)
    return(newx,newy)

def Aim(surface,tpower,tangle,stx,sty,tline):
    tline=[(Player_x,Player_y),pos]
    tpower=math.sqrt((tline[1][1]-tline[0][1])**2+(tline[1][0]-tline[0][0])**2)/5
    tangle=findAngle(pos,stx,sty)
    c1=TrajectoryPath(tangle,tpower,1,stx,sty)
    c2=TrajectoryPath(tangle,tpower,2,stx,sty)
    c3=TrajectoryPath(tangle,tpower,3,stx,sty)
    pygame.draw.circle(surface, (Color.Green),(stx,sty),5)
    pygame.draw.circle(surface,(Color.Green),c1,5)
    pygame.draw.circle(surface,(Color.Green),c2,5)
    pygame.draw.circle(surface,(Color.Green),c3,5)
#Map Loading
mapping=Map("Maps\Wating.tmx")
mapping.make_map()

#Game loop
isRunning=True
while isRunning==True:
    window.fill(Color.Black)
    mapping.render(window)
    pos=pygame.mouse.get_pos()
    window.blit(PlayerC,(Player_x,Player_y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isRunning= False
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                countJumps=1
            if event.key==pygame.K_LCTRL:
                countDash=0
            if event.key==pygame.K_r:
                if len(bullets)<10:
                    bullets.append(projectile(Player_x,Player_y,5,Color.Blue,power,time,angle,None,storex,storey))

    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Player_x-=Vel
        if keys[pygame.K_LCTRL]:
            DashLimit=Player_x+100
    if keys[pygame.K_d]:
        Player_x+=Vel

        
    #Jump Logic
    if countlimit==0:
        JumpLimit=Player_y-Tilesize*3+Size_y
    if keys[pygame.K_SPACE] and countJumps!=1:
        countlimit=1
        Player_y-=JVel
        if Player_y==JumpLimit:
            countJumps=1
    if countJumps==1:
        Player_y+=JVel
    if Player_y==Tilesize*3+Size_y:
        countJumps=0
        countlimit=0

        
    #Dash Logic
    if keys[pygame.K_LCTRL] and keys[pygame.K_a] and countDash!=1:
            countDash=1
            Player_x-=DVel
    if keys[pygame.K_LCTRL] and keys[pygame.K_d] and countDash!=1:
            countDash=1
            Player_x+=DVel

            
    #Projectile Logic
    if keys[pygame.K_r]:
        line=[(Player_x,Player_y),pos]
        storex=Player_x
        storey=Player_y
        time=0
        power=math.sqrt((line[1][1]-line[0][1])**2+(line[1][0]-line[0][0])**2)/5
        angle=findAngle(pos,storex,storey)
        Aim(window,power,angle,storex,storey,line)
    if keys[pygame.K_w]:
        print(Player_x,Player_y)
    for bullet in bullets:
        if bullet.y <Tilesize*3+Size_y + 50:
            bullet.time+=0.02
            bullet.po=bullet.ballPath()
            bullet.x=bullet.po[0]
            bullet.y=bullet.po[1]
        else:
            bullets.pop(bullets.index(bullet))
    for bullet in bullets:
        bullet.draw(window)
    
    pygame.display.update()
    pygame.display.flip()


