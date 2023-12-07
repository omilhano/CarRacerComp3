import pygame, random
from car import Car
from config import level2, pause_menu, level1_end
from healthbar import *
from hazards import Hazards
from zombie import Zombies
from garage import garage_screen
import sys


# TODO powerups

def start_level2():
    pygame.init()

    # defining screen/background
    bg = pygame.image.load(level2).convert_alpha()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Car Racing")
    # to run everything
    carryOn = True
    # to have game state
    game_active = True
    clock = pygame.time.Clock()

    # initialize car
    playerCar = Car(130, 680, 70)
    player_group = pygame.sprite.Group()
    player_group.add(playerCar)
    healthbar = Healthbar(5, 5, 300, 40, playerCar.health)
    # initialize hazards
    bloodspill = Hazards("spill", random.randint(1300, 1500),
                         random.choice([605, 682, 760]))
    level_cone = Hazards("small", random.randint(1300, 1500), random.choice([605, 682, 760]))
    hazard_sign = Hazards("tall", random.randint(1300, 1500), random.choice([605, 682, 760]))
    all_hazards = pygame.sprite.Group()
    all_hazards.add(bloodspill)
    all_hazards.add(level_cone)
    all_hazards.add(hazard_sign)

    # create zombies
    fastZombie = Zombies("fast", random.randint(1300, 1500), random.choice([605, 682, 760]))
    normalZombie = Zombies("normal", random.randint(1300, 1500), random.choice([605, 682, 760]))
    staticZombie = Zombies("static", random.randint(1300, 1500), random.choice([605, 682, 760]))

    all_zombies = pygame.sprite.Group()
    all_zombies.add(fastZombie)
    all_zombies.add(normalZombie)
    all_zombies.add(staticZombie)
    # initialize mouse

    # font
    corbelfont = pygame.font.SysFont('Corbel', 50)  # Select font and size

    def pause():
        loop = True
        pause_screen = pygame.image.load(pause_menu).convert_alpha()
        pausetext = corbelfont.render("Game is Paused", True, (100, 25, 225))
        spacebartext = corbelfont.render("Press Spacebar to continue", True, (100, 25, 225))
        screen.blit(pause_screen, [0, 0])
        screen.blit(pausetext, [200, 200])
        screen.blit(spacebartext, [200, 250])
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

    def level_end(): # Todo utils
        loop = True
        end_screen = pygame.image.load(level1_end).convert_alpha()
        screen.blit(end_screen, [0, 0])
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    garage_screen(playerCar, healthbar, 1)
            pygame.display.update()

    def check_collisions(playerCar, all_sprites):
        object_sprite = None
        for sprite in all_sprites:
            if pygame.sprite.collide_mask(playerCar, sprite) is None:
                pass
            else:
                object_sprite = sprite
        return object_sprite

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playerCar.moveUp()
                if event.key == pygame.K_s:
                    playerCar.moveDown()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerCar.moveLeft(5)
        if keys[pygame.K_d]:
            playerCar.moveRight(5)
        if keys[pygame.K_ESCAPE]:
            pause()

        if game_active:
            screen.blit(bg, (0, 0))
            # drawing the healthbar and score
            healthbar.draw(screen)
            playerCar.display_score(screen)
            playerCar.display_money(screen)
            # create hazards on road
            roadLane = 0
            for hazards in all_hazards:
                hazards.object_speed(random.randint(20, 30))
                if hazards.rect.right < 0:
                    playerCar.updateScore(50)
                    roadLane = random.randint(1, 3)
                    if roadLane == 1:
                        hazards.rect.center = [1300, 605]
                    elif roadLane == 2:
                        hazards.rect.center = [1300, 682]
                    else:
                        hazards.rect.center = [1300, 760]
            all_hazards.draw(screen)
            fastZombie.object_speed(random.randint(30, 40))
            normalZombie.object_speed(random.randint(20, 30))
            staticZombie.object_speed(random.randint(20, 30))
            for zombies in all_zombies:
                if zombies.can_spawn():
                    if zombies.rect.right < 0:
                        roadLane = random.randint(1, 3)
                        if roadLane == 1:
                            zombies.rect.center = [1300, 605]
                        elif roadLane == 2:
                            zombies.rect.center = [1300, 682]
                        else:
                            zombies.rect.center = [1300, 760]

            # collision logic
            hazard_collide = check_collisions(playerCar, all_hazards)
            if hazard_collide:
                if playerCar.get_damaged(hazard_collide):  # todo :3
                    game_active = False
                healthbar.hp = playerCar.health
            zombie_collide = check_collisions(playerCar, all_zombies)
            if zombie_collide:
                playerCar.get_money(zombie_collide)
            # Score testing variable
            if playerCar.score == 1000:
                level_end()
        else:
            from gameOver import gameover
            pygame.mixer.stop()
            gameover()

        # Number of frames per second e.g. 60
        clock.tick(60)
        all_zombies.draw(screen)
        # so its on top of everything
        player_group.draw(screen)
        # Refresh Screen
        pygame.display.flip()
        # this doesn't raise an error when quitting
    sys.exit()