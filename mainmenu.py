import sys
import os

from game_mode import game_intro
from load import continue_game
from rules import rules_p1
from settings import settings
from credits import credits_
from sounds import *
from cursor import Cursor
from config import main_menu
from utils import no_save_file


# Creating a function that creates the GUI
def menu():
    """
    Creates a loop that displays a custom screen
    Main menu with various buttons to take you to different screens
    :return: None
    """
    startingUp()
    # initiating pygames
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
    clock = pygame.time.Clock()

    while True:
        mouse = pygame.mouse.get_pos()
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                sys.exit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 475 <= mouse[0] <= 735 and 595 <= mouse[1] <= 712:
                    sys.exit()
            # press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 785 <= mouse[0] <= 1130 and 440 <= mouse[1] <= 595:
                    credits_()
            # pressing the play button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= mouse[0] <= 445 and 140 <= mouse[1] <= 295:
                    if os.path.exists("load.json"):
                        os.remove("load.json")
                    else:
                        print("The file does not exist")
                    game_intro()
            # pressing the continue game button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 787 <= mouse[0] <= 1130 and 138 <= mouse[1] <= 292:
                    try:
                        continue_game()
                    except:
                        no_save_file()
                    # pressing the settings button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 98 <= mouse[0] <= 445 and 443 <= mouse[1] <= 598:
                    settings()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 1105 <= mouse[0] <= 1275 and 760 <= mouse[1] <= 790:
                    rules_p1()

        # setting background
        bg = pygame.image.load(main_menu)
        screen.blit(bg, (0, 0))
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()
        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()
        # frames
        clock.tick(60)
