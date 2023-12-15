import sys
import pygame
from config import end_screen
from cursor import Cursor


def game_end():
    """
    Creates a loop that displays a custom screen letting
    the player know they finished tha game
    If player presses, menu button they return menu screen
    :return: None
    """
    pygame.init()

    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    while True:
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 1130 <= mouse[0] <= 1245 and 762 <= mouse[1] <= 800:
                    from mainmenu import menu
                    menu()
        bg = pygame.image.load(end_screen).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()
