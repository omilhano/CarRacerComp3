import pygame

from config import continue_scr


# TODO this, eventually

def continue_game():
    pygame.init()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    while True:
        bg = pygame.image.load(continue_scr).convert_alpha()
        screen.blit(bg, (0, 0))
        pygame.display.update()