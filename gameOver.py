import pygame

from cursor import Cursor
from level1 import start_level1


def gameover():
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
        bg = pygame.image.load("images/gameOver.png")
        screen.blit(bg, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1000 <= mouse_pos[0] <= 1265 and 650 <= mouse_pos[1] <= 780:
                    start_level1()
        pygame.display.flip()
