import sys

import pygame
from config import end_screen
from cursor import Cursor


def game_end():
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
            if ev.type == pygame.quit():
                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)

        bg = pygame.image.load(end_screen).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()
