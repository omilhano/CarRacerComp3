import pygame
import random
import sys
from car import Car
from config import level1
from healthbar import *
from hazards import Hazards
from powerUps import Invincible
from utils import pause
from visual_points import draw, display_time
from zombie import Zombies
from death import you_died


def play_multiplayer():
    pygame.init()

    # defining screen/background
    bg = pygame.image.load(level1).convert_alpha()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Driven to Decay : Byte the Dust")
    # to run everything
    carryOn = True
    # to have game state
    game_active = True
    clock = pygame.time.Clock()

    # initialize car
    playerCar = Car("car")
    playerBike = Car("bike")
    player_group = pygame.sprite.Group()
    player_group.add(playerCar)
    player_group.add(playerBike)
    car_healthbar = Healthbar(5, 5, playerCar.health)
    bike_healthbar = Healthbar(800, 5, playerBike.health)
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
    if not fastZombie.can_spawn():
        fastZombie.zombie_tp()
    normalZombie = Zombies("normal", random.randint(1300, 1500), random.choice([605, 682, 760]))
    if not normalZombie.can_spawn():
        fastZombie.zombie_tp()
    staticZombie = Zombies("static", random.randint(1300, 1500), random.choice([605, 682, 760]))
    if not staticZombie.can_spawn():
        fastZombie.zombie_tp()

    all_zombies = pygame.sprite.Group()
    all_zombies.add(fastZombie)
    all_zombies.add(normalZombie)
    all_zombies.add(staticZombie)

    # create power ups
    invincibility = Invincible(random.randint(1300, 1500), random.choice([605, 682, 760]))
    if not invincibility.can_spawn():
        invincibility.powerup_tp()
    all_powers = pygame.sprite.Group()
    all_powers.add(invincibility)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playerCar.move_up()
                if event.key == pygame.K_UP:
                    playerBike.move_up()
                if event.key == pygame.K_s:
                    playerCar.move_down()
                if event.key == pygame.K_DOWN:
                    playerBike.move_down()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerCar.move_left()
        if keys[pygame.K_LEFT]:
            playerBike.move_left()
        if keys[pygame.K_d]:
            playerCar.move_right()
        if keys[pygame.K_RIGHT]:
            playerBike.move_right()
        if keys[pygame.K_ESCAPE]:
            pause()

        if game_active:
            screen.blit(bg, (0, 0))
            display_time(screen)
            # drawing the healthbar
            draw(bike_healthbar, screen, "bike")
            draw(car_healthbar, screen, "car")
            # create hazards on road
            for hazards in all_hazards:
                hazards.object_speed(random.randint(20, 30))
                if hazards.rect.right < 0:
                    hazards.rect.center = [random.randint(1300, 1400), random.choice([605, 682, 760])]
                    check_if_stacked(hazards, all_hazards)

            fastZombie.object_speed(random.randint(30, 40))
            normalZombie.object_speed(random.randint(20, 30))
            staticZombie.object_speed(random.randint(20, 30))
            for zombies in all_zombies:
                if zombies.can_spawn():
                    if zombies.rect.right < 0:
                        zombies.rect.center = [random.randint(1300, 1400), random.choice([605, 682, 760])]

            invincibility.object_speed(random.randint(20, 30))
            for powers in all_powers:
                if powers.can_spawn():
                    if powers.rect.right < 0:
                        powers.rect.center = [random.randint(1300, 1400), random.choice([605, 682, 760])]

            # collision logic between car and obstacles
            powerup_collide = check_collisions(playerCar, all_powers)
            hazard_collide = check_collisions(playerCar, all_hazards)
            if hazard_collide:
                if playerCar.can_collide:
                    if playerCar.get_damaged(hazard_collide):
                        game_active = False
                    car_healthbar.hp = playerCar.health
            if powerup_collide:
                powerup_collide.affect_player(playerCar)
                if playerCar.health <= 0:
                    game_active = False
                car_healthbar.hp = playerCar.health
            zombie_collide = check_collisions(playerCar, all_zombies)
            if zombie_collide:
                playerCar.get_money(zombie_collide)

            powerup_collide = check_collisions(playerBike, all_powers)
            hazard_collide = check_collisions(playerBike, all_hazards)
            if hazard_collide:
                if playerBike.can_collide:
                    if playerBike.get_damaged(hazard_collide):
                        game_active = False
                    bike_healthbar.hp = playerBike.health
            if powerup_collide:
                powerup_collide.affect_player(playerBike)
                if playerCar.health <= 0:
                    game_active = False
                bike_healthbar.hp = playerBike.health
            zombie_collide = check_collisions(playerBike, all_zombies)
            if zombie_collide:
                playerBike.get_money(zombie_collide)

            playerBike.update_powerup()
            playerCar.update_powerup()

        else:
            from death import death_screen
            pygame.mixer.stop()
            you_died(2)

        # Number of frames per second e.g. 60
        clock.tick(60)
        all_powers.draw(screen)
        all_hazards.draw(screen)
        # so its on top of everything
        all_zombies.draw(screen)
        player_group.draw(screen)
        # Refresh Screen
        pygame.display.flip()


def check_collisions(player, all_sprites):
    """
        checks if the player collided with anything
        If so, returns what it collided with
        :param playerCar: object from class Car
        :param all_sprites: Group of Sprites from class Hazards, Zombies or PowerUp
        :return: None or object from class Hazards, Zombies or PowerUp
        """
    object_sprite = None
    for sprite in all_sprites:
        if pygame.sprite.collide_mask(player, sprite) is None:
            pass
        else:
            object_sprite = sprite
    return object_sprite


def check_if_stacked(hazard, all_hazards):
    """
        Checks if there's a hazard object on top of another hazard object
        if so, teleports the first hazard
        :param hazard: object from class Hazards
        :param all_hazards: Group of Sprites with all the hazards
        :return: None
        """
    for other_hazard in all_hazards:
        if pygame.sprite.collide_mask(hazard, other_hazard) is None:
            pass
        else:
            hazard.hazard_tp()
