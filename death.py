import sys
import pygame
from cursor import Cursor
from config import death_screen
from mainmenu import menu


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
                if 995 <= mouse[0] <= 1230 and 630 <= mouse[1] <= 775: #TODO button position
                    menu()
                if 995 <= mouse[0] <= 1230 and 630 <= mouse[1] <= 775: #TODO button position
                    from level1 import start_level1  # TODO solve circular import
                    start_level1()

        bg = pygame.image.load(death_screen).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()
