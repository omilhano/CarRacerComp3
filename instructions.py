import pygame

from config import intructions
from cursor import Cursor
from level1 import start_level1


def instructions():
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

    while True:
        bg = pygame.image.load(intructions)
        screen.blit(bg, (0, 0))
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                start_level1()
        pygame.display.flip()