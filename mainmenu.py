import pygame
from pygame import mixer
from level1 import start_level1
from instructions import instructions
from load import continue_game
from settings import settings
from credits import credits_
from sounds import *
from cursor import Cursor


# TODO Continue game button
# Creating a function that creates the GUI

def menu():
    startingUp()
    # initiating pygames
    pygame.init()
    # custom cursor image
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    # initialize at 1282x800
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    # name
    pygame.display.set_caption("Car Racer")
    #  continue screen temporarily
    continue_screen = pygame.image.load("images/inprogress.png")
    clock = pygame.time.Clock()

    while True:
        mouse = pygame.mouse.get_pos()
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 475 <= mouse[0] <= 735 and 595 <= mouse[1] <= 712:
                    pygame.quit()
            # press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 785 <= mouse[0] <= 1130 and 440 <= mouse[1] <= 595:
                    credits_()
            # pressing the play button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= mouse[0] <= 445 and 140 <= mouse[1] <= 295:
                    instructions()
            # pressing the continue game button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 787 <= mouse[0] <= 1130 and 138 <= mouse[1] <= 292:
                    continue_game()
                    # pressing the settings button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 98 <= mouse[0] <= 445 and 443 <= mouse[1] <= 598:
                    settings()

            # test position of the mouse
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())

        # setting background
        bg = pygame.image.load("images/menuimg.png")
        screen.blit(bg, (0, 0))
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()
        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()

        # frames
        clock.tick(60)
