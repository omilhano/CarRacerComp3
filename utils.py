import json
import sys
import pygame
from config import pause_menu, level1_end, no_save
from garage import garage_screen

pygame.init()

# defining screen
res = (1282, 800)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Driven to Decay: Byte the Dust")
# font
corbelfont = pygame.font.SysFont('Corbel', 50)  # Select font and size
clock = pygame.time.Clock()


def pause():
    """
    Creates variable "loop" and sets it as True
    Checks if pause is still activated with the while loop
    Functions blits the pause screen and pauses the game
    If space key is pressed the loop is exited and the game resumed

    :return: None
    """
    loop = True
    pause_screen = pygame.image.load(pause_menu).convert_alpha()
    screen.blit(pause_screen, [0, 0])
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    loop = False
        pygame.display.update()
        clock.tick(60)  # here so mouse can have movement


def level_end(level, playerCar, healthbar):
    """
    Creates variable "loop" and sets it as True
    Functions blits the end level screen and "pauses" the game
    If a key is pressed the loop is exited, the player is taken
    to the garage screen and the game is saved

    :param level: int level the player completed
    :param playerCar: object from class Car
    :param healthbar: object from class Healthbar
    :return: None
    """
    loop = True
    end_screen = pygame.image.load(end_screens[level]["image"]).convert_alpha()
    screen.blit(end_screen, [0, 0])
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                status = {"health": playerCar.health, "money": playerCar.money, "score": playerCar.score,
                          "level_completed": 1}
                with open("load.json", "w") as outfile:
                    json.dump(status, outfile)
                garage_screen(playerCar, healthbar, 1)
        pygame.display.update()


def no_save_file():
    """
    Creates variable "loop" and sets it as True
    Functions blits screen showing user there is no saved file created
    If a key is pressed the loop is exited and the player goes to mainmenu

    :return: None
    """
    loop = True
    end_screen = pygame.image.load(no_save).convert_alpha()
    screen.blit(end_screen, [0, 0])
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                from mainmenu import menu
                menu()
        pygame.display.update()


"""
Dictionary created for organization of level end screens
Ready for future implementation
"""
end_screens = {
    1: {"image": level1_end},

    # 2: {"image": level2_end},
    # 3: {"image": level3_end}
}
