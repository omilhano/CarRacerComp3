import sys
import pygame
from instructions import instructions
from config import intro_game
from cursor import Cursor


def game_intro():
    pygame.init()
    # custom cursor image
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    # initialize at 1282x800
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    # name
    pygame.display.set_caption("Driven to Decay : Byte the Dust")

    while True:
        bg = pygame.image.load(intro_game)
        screen.blit(bg, (0, 0))
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 475 <= mouse[0] <= 735 and 595 <= mouse[1] <= 725:
                    # back to menu
                    from mainmenu import menu
                    menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # single player
                if 47 <= mouse[0] <= 500 and 527 <= mouse[1] <= 594:
                    instructions(1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # multiplayer
                if 783 <= mouse[0] <= 1205 and 527 <= mouse[1] <= 595:
                    instructions(2)

        pygame.display.flip()
