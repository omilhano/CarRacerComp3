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
    #initialize at 1282x800
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
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
    corbelfont = pygame.font.SysFont('Corbel', 50)
    comicsansfont = pygame.font.SysFont("oswald", 50)
    game1_text = comicsansfont.render('Start The Game', True, blue)
    game2_text = corbelfont.render('Game2', True, blue)
    game3_text = corbelfont.render('Game3', True, blue)
    credits_text = corbelfont.render('credits', True, blue)
    quit_text = corbelfont.render('  quit', True, blue)

    title_text = comicsansfont.render('Computation III - Project', True, yellow)
    # interface loop
    pygame.mixer.music.stop()
    while True:
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
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 787 <= mouse[0] <= 1130 and 138 <= mouse[1] <= 292:
                    pass 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 98 <= mouse[0] <= 445 and 443 <= mouse[1] <= 598:
                    setting()
            #test position of the mouse
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())
        #setting bakcground
        bg = pygame.image.load("images/menuimg.png")
        screen.blit(bg,(0,0))
        # game 1 text
        mouse = pygame.mouse.get_pos()
        #teste zona start game
        pygame.draw.rect(screen, color_dark, [96, 139, 348, 157],2,3)

        #teste zona continue game
        pygame.draw.rect(screen, color_dark, [785, 135, 350, 157],2,3)
        
        #teste zona de settings
        pygame.draw.rect(screen, color_dark, [96, 4 * 111, 350, 157 ],2,3)
        # teste zona rectangulo creditos
        pygame.draw.rect(screen, color_dark, [785, 4 * 110, 350, 157], 2,3)

        #teste zona rectangulo quit
        pygame.draw.rect(screen, color_dark,(475, 5 * 119, 260, 120),2, 3)
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