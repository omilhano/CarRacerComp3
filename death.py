import sys
import pygame
from cursor import Cursor
from config import death_screen


def you_died():
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
            # press on menu button to go back
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 880 <= mouse[0] <= 1264 and 720 <= mouse[1] <= 785:
                    from mainmenu import menu
                    menu()
                if 32 <= mouse[0] <= 275 and 720 <= mouse[1] <= 785:
                    from level1 import start_level1  # TODO solve circular import
                    start_level1()
                # test position of the mouse
                # if ev.type == pygame.MOUSEBUTTONDOWN:
                #     print(pygame.mouse.get_pos())

        bg = pygame.image.load(death_screen).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()
