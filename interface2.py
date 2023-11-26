import pygame
from pygame.locals import *
from pygame import mixer
from mainmenu import menu


#starting music
mixer.init()
mixer.music.load("soundtrackmenu.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
# Creating a function that creates the GUI
def interface():
    pygame.init()
    #setting game icon
    icon = pygame.image.load('images/icon.png') 
    pygame.display.set_icon(icon)
    #initialize at certain res
    res = (1282,800)
    screen = pygame.display.set_mode((res))
    pygame.display.set_caption("Driven to Decay : Byte the Dust")
    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            elif ev.type == pygame.KEYDOWN:
            # Check if ENTER/Return is KEYDOWN
                if ev.key == pygame.K_RETURN:
                    mixer.music.load("enginerev.mp3")
                    mixer.music.set_volume(0.7)
                    mixer.music.play()
                    pygame.time.delay(1000)
                    menu()
        # setting the background as image
        bg = pygame.image.load("images/titlemenu.png")
        # startmenu = pygame.image.load("pressthis.png").convert_alpha()
        #INSIDE OF THE GAME LOOP
        screen.blit(bg,(0,0))
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()
