import pygame
from Scripts.utilities import *
from Scripts.Colors import *
pygame.init()
def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800,600
    window_title = "The Last Samurai"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
create_window()

#Create Buttons
ExitButton=Button("Graphics\Me.png",200,100)
PlayButton=Button("Graphics\download.jpg",100,100)
#Create Text
menu_title=Text(12,"Title",Color.White,1,1,window_width/2,window_height/2,32)

#Create Menu
def Main():
    window.fill(Color.Black)
    menu_title.Display_Text(window)
    PlayButton.DisplayButton(window)
def Option():
    window.fill(Color.Black)
    ExitButton.DisplayButton(window)
    
MenuLoop=True
while MenuLoop==True:
    Main()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            if PlayButton.isOver(pos):
                Optionloop=True
                while Optionloop==True:
                    Option()
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos=pygame.mouse.get_pos()
                            if ExitButton.isOver(pos):
                                Optionloop=False
                                Main()


    pygame.display.update()
    pygame.display.flip()
