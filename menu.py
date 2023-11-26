import pygame
import sys
from game import car_racing
from setting import setting

#TODO Start game button
#TODO Continue game button
#TODO Credits buttons
#TODO Exit button
#TODO Settings button another screen


# Creating a function that creates the GUI
def menu():
    # initiating pygames
    pygame.init()
    #making cursor invisible
    pygame.mouse.set_visible(False) 
    #custom cursor image
    custom_cursor = pygame.image.load('images/cursor.png').convert_alpha()
    #initialize at 1282x800
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    #name
    pygame.display.set_caption("Car Racer")
    # interface loop
    pygame.mixer.music.stop()
   
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
                    setting()

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
                    menu()
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