import pygame


def continue_game():
    pygame.init()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    while True:
        bg = pygame.image.load("images/inprogress.png").convert_alpha()
        screen.blit(bg, (0, 0))
        pygame.display.update()