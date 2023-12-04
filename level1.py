import pygame, random
from car import Car
from healthbar import *
from hazards import Hazards
from zombie import Zombies
from garage import garage_screen


# TODO powerups
# TODO zombies

def start_level1():
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
    playerCar = Car(130, 680, 70)
    player_group = pygame.sprite.Group()
    player_group.add(playerCar)
    healthbar = Healthbar(5, 5, 300, 40, playerCar.health)

    # initialize hazards
    bloodspill_img = pygame.image.load("images/blood_spill_lv1.png").convert_alpha()
    level_cone_img = pygame.image.load("images/traficcone_lv1.png").convert_alpha()
    danger_sign = pygame.image.load("images/hazard_roadsignlv1.png").convert_alpha()
    bloodspill = Hazards(1000, 680, 5, bloodspill_img, "bloodspill")
    level_cone = Hazards(1200, 608, 5, level_cone_img, "level_cone")
    hazard_sign = Hazards(1500, 760, 5, danger_sign, "hazard_sign")
    all_hazards = pygame.sprite.Group()
    all_hazards.add(bloodspill)
    all_hazards.add(level_cone)
    all_hazards.add(hazard_sign)

    # create zombies
    fastZombie = Zombies("fast", 1280, random.choice([605, 682, 760]))
    fastZombie.assign_attributes()

    normalZombie = Zombies("normal", 1300, random.choice([605, 682, 760]))
    normalZombie.assign_attributes()

    staticZombie = Zombies("static", 1400, random.choice([605, 682, 760] ))
    staticZombie.assign_attributes()

    all_zombies = pygame.sprite.Group()
    all_zombies.add(fastZombie)
    all_zombies.add(normalZombie)
    all_zombies.add(staticZombie)
    # initialize mouse

    # font
    corbelfont = pygame.font.SysFont('Corbel', 50)  # Select font and size

    def pause():
        loop = True
        bg = pygame.image.load("images/inprogress.png").convert_alpha()
        pausetext = corbelfont.render("Game is Paused", True, (100, 25, 225))
        spacebartext = corbelfont.render("Press Spacebar to continue", True, (100, 25, 225))
        screen.blit(bg, [0, 0])
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
                        bg = pygame.image.load("images/level1bg.jpg").convert()
            pygame.display.update()
            clock.tick(60)

    def display_score():
        current_score = playerCar.score
        score_surface = corbelfont.render(f" Score:{current_score}", False, (197, 136, 215))
        score_rect = score_surface.get_rect(center=(400, 30))
        screen.blit(score_surface, score_rect)

    def check_collisions(playerCar, all_hazards):
        tester = ""
        for sprite in all_hazards:
            if pygame.sprite.collide_mask(playerCar, sprite) is None:
                pass
            else:
                tester = sprite.getType()
        return tester

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
            display_score()
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
            staticZombie.object_speed(random.randint(20,30))
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
            if check_collisions(playerCar, all_hazards) == "bloodspill":
                playerCar.change_rand_lane()
            elif check_collisions(playerCar, all_hazards) == "level_cone":
                if playerCar.get_damaged(5):
                    game_active = False
                else:
                    healthbar.hp = playerCar.health
                    level_cone.rect.center = [1400, random.choice([605, 682, 760])]
            elif check_collisions(playerCar, all_hazards) == "hazard_sign":
                if playerCar.get_damaged(5):
                    game_active = False
                else:
                    healthbar.hp = playerCar.health
                    hazard_sign.rect.center = [1400, random.choice([605, 682, 760])]
            # test position
            # print(playerCar.rect.x)
            # print(playerCar.rect.y)

            # Score testing variable
            if playerCar.score == 200:
                garage_screen(playerCar, healthbar, 1)
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
    pygame.quit()
