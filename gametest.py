import pygame
from car_test import Car
from healthbar import *


def car_racing():
    pygame.init()

    # defining screen/background
    bg = pygame.image.load("images/level1bg.jpg").convert()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Car Racing")
    # to run everything
    carryOn = True
    # to have game state
    game_active = True
    clock = pygame.time.Clock()

    # initialize car
    MAX_CAR_HP = 100
    playerCar = Car(130, 680, 70, MAX_CAR_HP)
    player_group = pygame.sprite.Group()
    player_group.add(playerCar)
    healthbar = Healthbar(5, 5, 300, 40, MAX_CAR_HP)

    # font
    corbelfont = pygame.font.SysFont('Corbel', 50)  # Select font and size
    # for utils
    start_time = 0

    def pause():
        game_active = False
        loop = True
        pausetext = corbelfont.render("Game is Paused", True, (100, 25, 225))
        spacebartext = corbelfont.render("Press Spacebar to continue", True, (100, 25, 225))
        screen.blit(pausetext, [200, 200])
        screen.blit(spacebartext, [200, 250])
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill((0, 0, 0))
                        loop = False
            pygame.display.update()
            clock.tick(60)

    def display_score():
        current_time = int(pygame.time.get_ticks() / 1000) - start_time
        score_surface = corbelfont.render(f" Score:{current_time}", False, (197, 136, 215))
        score_rect = score_surface.get_rect(center=(400, 30))
        screen.blit(score_surface, score_rect)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                # damage taker test
                if event.key == pygame.K_f:
                    if playerCar.get_damaged(5):
                        game_active = False
                    else:
                        healthbar.hp -= 5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerCar.moveLeft(5)
        if keys[pygame.K_d]:
            playerCar.moveRight(5)
        if keys[pygame.K_w]:
            playerCar.moveBackward(5)
        if keys[pygame.K_s]:
            playerCar.moveForward(5)
        if keys[pygame.K_ESCAPE]:
            pause()

        if game_active:

            screen.blit(bg, (0, 0))
            display_score()
            # drawing the healthbar
            healthbar.draw(screen)
            # test position
            # print(playerCar.rect.x)
            # print(playerCar.rect.y)
            player_group.draw(screen)
        else:
            # TODO GAME OVER MENU
            start_time = int(pygame.time.get_ticks() / 1000)
            screen.fill((0, 0, 0))

        # Number of frames per second e.g. 60
        clock.tick(60)
        # Refresh Screen
        pygame.display.flip()
    pygame.quit()
