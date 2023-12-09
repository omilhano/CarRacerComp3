import sys
import pygame
from config import garage
from cursor import Cursor
from level2 import start_level2
from visual_points import draw, display_score, display_money


# TODO define powerups
def garage_screen(playerCar, healthbar, level):
    pygame.init()

    # defining screen/background
    bg = pygame.image.load(garage).convert_alpha()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Car Racing")
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    clock = pygame.time.Clock()

    def recover_health():
        if playerCar.health <= 90:
            playerCar.health += 10
            healthbar.hp = playerCar.health
        elif playerCar.health + 10 > 100:
            playerCar.health = 100
            healthbar.hp = playerCar.health

    def buy_health():
        if playerCar.health == 100: #added this
            if playerCar.money - 5 > -1:
                playerCar.money -= 5
                recover_health()

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
                    buy_health()

            # test position of the mouse
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())

        # setting background
        screen.blit(bg, (0, 0))
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()
        draw(healthbar, screen)
        display_score(playerCar.score, screen)
        display_money(playerCar.money, screen)

        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()

        # frames
        clock.tick(60)
