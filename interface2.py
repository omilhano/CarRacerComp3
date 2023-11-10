import pygame
import sys
from game import car_racing
from pygame.locals import *
from pygame import mixer


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
    #change name ? placeholder
    pygame.display.set_caption("Car Racer")
    # creatinbg some colors (RGB scale)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    # creating some textlabels
    # corbelfont = pygame.font.SysFont('Corbel', 50)
    # comicsansfont = pygame.font.SysFont("oswald", 50)
    # game1_text = comicsansfont.render('Start The Game', True, blue)
    # game2_text = corbelfont.render('Game2', True, blue)
    # game3_text = corbelfont.render('Game3', True, blue)
    # credits_text = corbelfont.render('credits', True, blue)
    # quit_text = corbelfont.render('  quit', True, blue)
    # title_text = comicsansfont.render('Computation III - Project', True, yellow)
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
                    car_racing()
        # setting the background as image
        bg = pygame.image.load("maxresdefault.jpg")
        # startmenu = pygame.image.load("pressthis.png").convert_alpha()
        #INSIDE OF THE GAME LOOP
        screen.blit(bg,(0,0))

        # print the buttons text and the box(color changing)
        # game 1 text
        mouse = pygame.mouse.get_pos()
        # when the mouse is on the box it changes color
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()


def credits_():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    corbelfont = pygame.font.SysFont('Corbel', 50)
    back_text = corbelfont.render('   back', True, blue)
    comicsansfont = pygame.font.SysFont('arial', 25)
    line1_text = comicsansfont.render('Davide Farinati, dfarinati@novaims.unl.pt', True, yellow)
    line2_text = comicsansfont.render('Joao Fonseca, jfonseca@novaims.unl.pt', True, yellow)
    line3_text = comicsansfont.render('Liah Rosenfeld, lrosenfeld@novaims.unl.pt', True, yellow)

    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[
                    1] <= 5 * 120 + 60:
                    interface()
        screen.fill((0, 0, 0))
        # credits text
        screen.blit(line1_text, (0, 0))
        screen.blit(line2_text, (0, 25))
        screen.blit(line3_text, (0, 50))
        # back text
        if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
            pygame.draw.rect(screen, red, [450, 5 * 120, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [450, 5 * 120, 140, 60])
        screen.blit(back_text, (450, 5 * 120))

        pygame.display.update()