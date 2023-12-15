import sys
import pygame
from cursor import Cursor
from config import death_screen


def you_died(number):
    """
    Creates a loop that displays a custom background letting the player know
    they lost the game
    Mouse position is checked to give buttons a function leading the player to
    the mainmenu or starting over from level 1

    :param number: int used to check if singleplayer or multiplayer
    :return: None
    """
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
                    if number == 1:
                        from level1 import start_level1
                        start_level1()
                    else:
                        from multiplayer import play_multiplayer
                        play_multiplayer()

        bg = pygame.image.load(death_screen).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()
