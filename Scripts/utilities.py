import pygame
from Scripts.Colors import *
pygame.init()

class Button():
    def __init__(self,Image,buttonpos_x,buttonpos_y):
        self.button = pygame.image.load(Image).convert_alpha()
        self.buttonpos_x=buttonpos_x
        self.buttonpos_y=buttonpos_y
    def DisplayButton(self,screen):
        screen.blit(self.button,(self.buttonpos_x,self.buttonpos_y))
    def isOver(self,pos):
        mask=pygame.mask.from_surface(self.button)
        try:
            if mask.get_at((pos[0]-self.buttonpos_x, pos[1]-self.buttonpos_y)):
                return True
        except IndexError:
            pass
        return False
        
#class Input_Box():
        
class Text():
    def __init__(self,image,write,color,ipos_x,ipos_y,tpos_x,tpos_y,tsize):#ipos stand for image position
        global text
        self.image=image
        self.write=write                                      #tpos stand for text position
        self.color=color
        self.ipos_x=ipos_x
        self.ipos_y=ipos_y
        self.tpos_x=tpos_x
        self.tpos_y=tpos_y
        self.tsize=tsize
        font=pygame.font.Font("freesansbold.ttf",self.tsize)
        text=font.render(self.write,True,self.color)
    def Display_Text(self,surface):
        surface.blit(text,(self.tpos_x,self.tpos_y))
            
            
  
