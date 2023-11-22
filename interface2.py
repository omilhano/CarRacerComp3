import pygame
import sys
from game import car_racing
from pygame.locals import *
from pygame import mixer
from menu import menu


#starting music
mixer.init()
mixer.music.load("soundtrackmenu.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
# Creating a function that creates the GUI
def interface():
    pygame.init()
    #initialize at certain res
    res = (1280,618)
    screen = pygame.display.set_mode((res))
    pygame.display.set_caption("Driven to Decay : Byte the Dust")
    # interface loop
    keys = pygame.key.get_pressed()
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.KEYDOWN:
            # Check if ENTER/Return is KEYDOWN
                if ev.key == pygame.K_RETURN:
                    menu()
        # setting the background as image
        bg = pygame.image.load("images/menu.png")
        # startmenu = pygame.image.load("pressthis.png").convert_alpha()
        #INSIDE OF THE GAME LOOP
        screen.blit(bg,(0,0))
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()
