import pygame
from pygame import mixer
from gametest import car_racing
from settings import settings
from credits import credits_
from sounds import *
# TODO Continue game button
# Creating a function that creates the GUI

def menu():
    global first_time #TODO this is a brute way to force it but doesnt work, we will need a config file to fix this
    if first_time:
        startingUp()
    # initiating pygames
    pygame.init()
    #custom cursor image
    custom_cursor = pygame.image.load('images/cursor.png').convert_alpha()
    #initialize at 1282x800
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    #name
    pygame.display.set_caption("Car Racer")
    #music control
    # pygame.mixer.music.stop()
    # mixer.music.unload()
    # mixer.music.load("musicbackground.mp3")
    # mixer.music.set_volume(volume)
    # mixer.music.play()
    
    clock=pygame.time.Clock()
   
    while True: 
        mouse = pygame.mouse.get_pos()
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 475 <= mouse[0] <= 735 and 595<= mouse[1] <= 712:
                    pygame.quit()
            # press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 785 <= mouse[0] <= 1130 and 440 <= mouse[1] <= 595:
                    credits_()
            # pressing the play button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= mouse[0] <= 445 and 140 <= mouse[1] <= 295:
                    car_racing()
            #pressing the continue game button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 787 <= mouse[0] <= 1130 and 138 <= mouse[1] <= 292:
                    pass 
            #pressing the settings button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 98 <= mouse[0] <= 445 and 443 <= mouse[1] <= 598:
                    settings()

            #test position of the mouse
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())
        #setting bakcground
        bg = pygame.image.load("images/menuimg.png")
        screen.blit(bg,(0,0))
        #making image appear in cursor place
        screen.blit( custom_cursor, mouse ) 
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.flip()

        #frames
        clock.tick(120)