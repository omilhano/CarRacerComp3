import sys
import pygame
from cursor import Cursor
from config import credits_screen


def credits_():
    """
    Page where the creators are credited
    Sets the cursor as a custom image
    Sets the resolution of the screen
    Creates a while loop, which is only exited when the screen is quit or
    A button is clicked where it calls the menu function from the file mainmenu.py
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
                if 1135 <= mouse[0] <= 1235 and 760 <= mouse[1] <= 790:
                    from mainmenu import menu
                    menu()

        bg = pygame.image.load(credits_screen).convert_alpha()
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()
