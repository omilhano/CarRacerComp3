import sys

import pygame
from pygame import mixer
from config import settings_screen

from cursor import Cursor
from sounds import *

# TODO changes volume buttons sizes
# Creating a function that creates the GUI
def settings():
    from mainmenu import menu # TODO liahh
    # initiating pygame
    pygame.init()
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    # initialize at 720x720
    res = (974, 974)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Settings")
    # interface 
    while True:
        mouse = pygame.mouse.get_pos()
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 275 <= mouse[0] <= 315 and 515 <= mouse[1] <= 560:
                    # mute and play
                    pause()  # this just turns off and on the song, doesnt actually pause
                if 600 <= mouse[0] <= 655 and 515 <= mouse[1] <= 545:
                    menu()
                if 270 <= mouse[0] <= 290 and 428 <= mouse[1] <= 433:
                    lower_volume()
                if 620 <= mouse[0] <= 642 and 420 <= mouse[1] <= 445:
                    increase_volume()
        # setting the background color as black
        bg = pygame.image.load(settings_screen).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()

        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()
