import pygame, random
from car_test import Car


def car_racing():
    pygame.init()

    # defining screen/background
    bg = pygame.image.load("images/level1bg.jpg").convert()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Car Racing")
    carryOn = True
    clock = pygame.time.Clock()
    playerCar = Car(130, 680, 70)
    player_group = pygame.sprite.Group()
    player_group.add(playerCar)

    def pause():
        loop = True
        corbelfont = pygame.font.SysFont('Corbel', 50)  # Select font and size
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

    speed = 1  # TODO what is this

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    playerCar.moveRight(10)

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

        screen.blit(bg, (0, 0))
        print(playerCar.rect.x)
        print(playerCar.rect.y)
        player_group.draw(screen)
        # Refresh Screen
        pygame.display.flip()
        # Number of frames per second e.g. 60
        clock.tick(60)

    pygame.quit()
