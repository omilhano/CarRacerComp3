import sys
import pygame
from config import rules_1, rules_2
from cursor import Cursor


def rules_p1():
    pygame.init()
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    # initialize at 720x720
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Settings")

    # interface
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 23 <= mouse[0] <= 125 and 700 <= mouse[1] <= 780:  # TODO alex please check buttons
                    from mainmenu import menu
                    menu()
                if 1180 <= mouse[0] <= 1270 and 750 <= mouse[1] <= 785:  # TODO alex please check buttons
                    rules_p2()
        bg = pygame.image.load(rules_1).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()

        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()


def rules_p2():
    pygame.init()
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    # initialize at 720x720
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Full Rules")

    # interface
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= mouse[0] <= 110 and 755 <= mouse[1] <= 780:  # TODO alex please check buttons
                    rules_p1()
        bg = pygame.image.load(rules_2).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()

        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()
