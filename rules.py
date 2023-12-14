import sys

import pygame

from config import rules_1
from cursor import Cursor


def rules_p1():
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
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                sys.exit()

        bg = pygame.image.load(rules_1).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()

        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()
