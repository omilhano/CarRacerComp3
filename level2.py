import sys
import pygame, random
from hazards import Hazards
from gameOver import gameover
from config import level2, oil_spill, bear_trap, road_sign_lv2, pause_menu, level1
from visual_points import draw, display_score, display_money
from zombie import Zombies


# TODO powerups
# TODO zombies

def start_level2(playerCar, healthbar):
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

    player_group = pygame.sprite.Group()
    player_group.add(playerCar)
    # initialize hazards
    oilspill = Hazards("spill", random.randint(1300, 1500),
                       random.choice([605, 682, 760]))
    beartrap = Hazards("beartrap", random.randint(1300, 1500),
                       random.choice([605, 682, 760]))  # TODO change to correct
    hazard_sign = Hazards("tall", random.randint(1300, 1500), random.choice([605, 682, 760]))

    all_hazards = pygame.sprite.Group()
    all_hazards.add(oilspill)
    all_hazards.add(beartrap)
    all_hazards.add(hazard_sign)

    # create zombies
    fastZombie = Zombies("fast", random.randint(1300, 1500), random.choice([605, 682, 760]))
    normalZombie = Zombies("normal", random.randint(1300, 1500), random.choice([605, 682, 760]))
    staticZombie = Zombies("static", random.randint(1300, 1500), random.choice([605, 682, 760]))

    all_zombies = pygame.sprite.Group()
    all_zombies.add(fastZombie)
    all_zombies.add(normalZombie)
    all_zombies.add(staticZombie)

    def check_collisions(playerCar, all_sprites):
        object_sprite = None
        for sprite in all_sprites:
            if pygame.sprite.collide_mask(playerCar, sprite) is None:
                pass
            else:
                object_sprite = sprite
        return object_sprite

    def check_if_stacked(hazard):
        for other_hazard in all_hazards:
            if pygame.sprite.collide_mask(hazard, other_hazard) is None:
                pass
            else:
                hazard.hazard_tp()

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                # damage taker test
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
            pass

        if game_active:
            screen.blit(bg, (0, 0))
            # drawing the healthbar and score
            draw(healthbar, screen)
            display_score(playerCar.score, screen)
            display_money(playerCar.money, screen)

            # create hazards on road
            for hazards in all_hazards:
                hazards.object_speed(random.randint(20, 30))
                if hazards.rect.right < 0:
                    playerCar.updateScore(hazards.hazard_type)
                    hazards.rect.center = [random.randint(1300, 1400), random.choice([605, 682, 760])]
                    check_if_stacked(hazards)
            all_hazards.draw(screen)

            fastZombie.object_speed(random.randint(30, 40))
            normalZombie.object_speed(random.randint(20, 30))
            staticZombie.object_speed(random.randint(20, 30))
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

            # collision logic between car and obstacles
            hazard_collide = check_collisions(playerCar, all_hazards)
            if hazard_collide:
                if playerCar.get_damaged(hazard_collide):  # todo :3
                    game_active = False
                healthbar.hp = playerCar.health
            zombie_collide = check_collisions(playerCar, all_zombies)
            if zombie_collide:
                playerCar.get_money(zombie_collide)
            # Score testing variable
            if playerCar.score > 400:
                from utils import level_end # TODO this is  NOT a circular import wtf
                level_end(2, playerCar, healthbar)

            playerCar.update_movement()
        else:
            # TODO GAME OVER MENU
            pygame.mixer.stop()
            gameover()
            pass

        # Number of frames per second e.g. 60
        clock.tick(60)
        # so its on top of everything
        player_group.draw(screen)
        # Refresh Screen
        pygame.display.flip()
    sys.exit() # TODO death
