import sys
import pygame
from config import instructions_single, instructions_multi
from cursor import Cursor
from level1 import start_level1
from multiplayer import play_multiplayer


def instructions(players):
    """
    Creates a screen with simplified instructions, displays a different screen if
    one or two people are playing
    Will proceed to corresponding gamemode when any key is pressed
    :param players: number of players, used to see if its multiplayer
    :return: None
    """
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
        if players == 1:
            bg = pygame.image.load(instructions_single)
        else:
            bg = pygame.image.load(instructions_multi)
        screen.blit(bg, (0, 0))
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if players == 1:
                    start_level1()
                else:
                    play_multiplayer()
        pygame.display.flip()
