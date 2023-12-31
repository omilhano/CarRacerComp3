import sys
import time
import pygame, random

from death import you_died
from hazards import Hazards
from config import level2
from powerUps import BearTrap, Invincible, SlowTime
from theend import game_end
from visual_points import draw, display_score, display_money
from zombie import Zombies


def start_level2(playerCar, healthbar):
    """
    The first level of the game
    :param playerCar: object of class Car
    :param healthbar: object of class Healthbar
    :return: None
    """
    pygame.init()

    # defining screen/background
    bg = pygame.image.load(level2).convert_alpha()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Driven to Decay : Byte the Dust")
    # to run everything
    carryOn = True
    # to have game state
    game_active = True
    clock = pygame.time.Clock()

    # variable specific to see if time is slowed
    time_slowed = False
    status_change_time = 0
    player_group = pygame.sprite.Group()
    player_group.add(playerCar)
    # initialize hazards
    oilspill = Hazards("spill", random.randint(1300, 1500),
                       random.choice([605, 682, 760]))
    hazard_sign = Hazards("tall", random.randint(1300, 1500), random.choice([605, 682, 760]))

    all_hazards = pygame.sprite.Group()
    all_hazards.add(oilspill)
    all_hazards.add(hazard_sign)

    # defining powerups
    invincibility = Invincible(random.randint(1300, 1500), random.choice([605, 682, 760]))
    if not invincibility.can_spawn():
        invincibility.powerup_tp()
    all_powers = pygame.sprite.Group()
    beartrap = BearTrap(random.randint(1300, 1500), random.choice([605, 682, 760]))
    if not beartrap.can_spawn():
        beartrap.powerup_tp()
    slow_time = SlowTime(random.randint(1300, 1500), random.choice([605, 682, 760]))
    if not slow_time.can_spawn():
        beartrap.powerup_tp()
    all_powers.add(slow_time)
    all_powers.add(beartrap)
    all_powers.add(invincibility)

    # create zombies
    fastZombie = Zombies("fast", random.randint(1300, 1500), random.choice([605, 682, 760]))
    normalZombie = Zombies("normal", random.randint(1300, 1500), random.choice([605, 682, 760]))
    staticZombie = Zombies("static", random.randint(1300, 1500), random.choice([605, 682, 760]))

    all_zombies = pygame.sprite.Group()
    all_zombies.add(fastZombie)
    all_zombies.add(normalZombie)
    all_zombies.add(staticZombie)

    def check_collisions(playerCar, all_sprites):
        """
        Checks if player collided with a sprite
        If True, returns what it collided with
        :param playerCar: object of class Car
        :param all_sprites: Group of Sprites from class Hazards, Zombies or PowerUp
        :return: None or object from class Hazards, Zombies or PowerUp
        """
        object_sprite = None
        for sprite in all_sprites:
            if pygame.sprite.collide_mask(playerCar, sprite) is None:
                pass
            else:
                object_sprite = sprite
        return object_sprite

    def check_if_stacked(hazard, all_hazards):
        """
        Checks if there is a hazard object on top of another hazard object
        If True, teleports the first hazard
        :param hazard: object of class Hazard
        :param all_hazards: Group of sprites with all the hazards
        :return: None
        """
        for other_hazard in all_hazards:
            if pygame.sprite.collide_mask(hazard, other_hazard) is None:
                pass
            else:
                hazard.hazard_tp()

    def update_traffic():
        """
        Checks if time is not affected and if
        Checks if 5 seconds have passed since the player collided
        with the powerup SlowTime
        Revers the change done to sprites
        :return: None
        """
        if not time_slowed and time.time() > status_change_time + 5:
            for zombie in all_zombies:
                zombie.return_normal()
            for hazard in all_hazards:
                hazard.return_normal()
            for power in all_powers:
                power.return_normal()

    while carryOn:
        # check for inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # damage taker test
                if event.key == pygame.K_w:
                    playerCar.move_up()
                if event.key == pygame.K_s:
                    playerCar.move_down()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerCar.move_left()
        if keys[pygame.K_d]:
            playerCar.move_right()
        if keys[pygame.K_ESCAPE]:
            pass

        if game_active:
            screen.blit(bg, (0, 0))
            # drawing the healthbar and score
            draw(healthbar, screen, "car")
            display_score(playerCar.score, screen)
            display_money(playerCar.money, screen)

            # create hazards on road
            for hazard in all_hazards:
                hazard.object_speed(random.randint(20, 30))
                if hazard.rect.right < 0:
                    playerCar.update_score(hazard)
                    hazard.rect.center = [random.randint(1300, 1400), random.choice([605, 682, 760])]
                    check_if_stacked(hazard, all_hazards)
            all_hazards.draw(screen)

            fastZombie.object_speed(random.randint(30, 40))
            normalZombie.object_speed(random.randint(20, 30))
            staticZombie.object_speed(random.randint(20, 30))

            # zombie spawn logic
            for zombies in all_zombies:
                if zombies.can_spawn():
                    if zombies.rect.right < 0:
                        roadLane = random.randint(1, 3)
                        if roadLane == 1:
                            zombies.rect.center = [random.randint(1400, 1500) + 40, 605]
                        elif roadLane == 2:
                            zombies.rect.center = [random.randint(1400, 1500) + 50, 682]
                        else:
                            zombies.rect.center = [random.randint(1400, 1500) + 120, 760]

            invincibility.object_speed(random.randint(20, 30))
            beartrap.object_speed(random.randint(20, 30))
            slow_time.object_speed(random.randint(15, 20))

            # powerup spawn logic
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
                    healthbar.hp = playerCar.health
            if powerup_collide:
                powerup_collide.affect_player(playerCar)
                powerup_collide.affect_traffic(all_zombies, all_hazards, all_powers)
                status_change_time = time.time()
                if playerCar.health <= 0:
                    game_active = False
                healthbar.hp = playerCar.health
            zombie_collide = check_collisions(playerCar, all_zombies)
            if zombie_collide:
                playerCar.get_money(zombie_collide)

            playerCar.update_powerup()
            update_traffic()
            if playerCar.score > 2000:
                game_end()

            playerCar.update_movement()
        else:
            pygame.mixer.stop()
            you_died(1)
            pass

        # Number of frames per second e.g. 60
        clock.tick(60)
        all_zombies.draw(screen)
        all_powers.draw(screen)
        # so its on top of everything
        player_group.draw(screen)
        # Refresh Screen
        pygame.display.flip()
