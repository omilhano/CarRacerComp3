import sys
import pygame
from config import garage
from cursor import Cursor
from level2 import start_level2
from visual_points import draw, display_score, display_money


def garage_screen(playerCar, healthbar, level):
    """

    :param playerCar: object of class Car
    :param healthbar: object of class Healthbar
    :param level: int level the player completed
    :return: None
    """
    pygame.init()

    # defining screen/background
    bg = pygame.image.load(garage).convert_alpha()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Driven to Decay : Byte the Dust")
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    clock = pygame.time.Clock()

    while True:
        mouse = pygame.mouse.get_pos()
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                sys.exit()
            # press the continue button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 1000 <= mouse[0] <= 1230 and 725 <= mouse[1] <= 760:
                    if level == 1:
                        start_level2(playerCar, healthbar)
                    elif level == 2:
                        pass  # start_level3(playerCar, healthbar)
            # pressing the buying button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 219 <= mouse[0] <= 365 and 338 <= mouse[1] <= 396:
                    buy_health(playerCar, healthbar)
                if 32 <= mouse[0] <= 315 and 727 <= mouse[1] <= 765:
                    from mainmenu import menu
                    menu()

        # setting background
        screen.blit(bg, (0, 0))
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()
        draw(healthbar, screen, "car")
        display_score(playerCar.score, screen)
        display_money(playerCar.money, screen)

        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()

        # frames
        clock.tick(60)


def recover_health(player, healthbar):
    if player.health <= 90:
        player.health += 10
        healthbar.hp = player.health
    elif player.health + 10 > 100:
        player.health = 100
        healthbar.hp = player.health


def buy_health(player, healthbar):
    if player.health != 100:  # added this
        if player.money - 5 > -1:
            player.money -= 5
            recover_health(player, healthbar)
