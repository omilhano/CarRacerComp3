import sys
import pygame, random
from hazards import Hazards
from gameOver import gameover
from config import level2, oil_spill, bear_trap, road_sign_lv2, pause_menu, level1


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
    oilspill_img = pygame.image.load(oil_spill).convert_alpha()
    beartrap_img = pygame.image.load(bear_trap).convert_alpha()
    roadsign_img = pygame.image.load(road_sign_lv2).convert_alpha()
    oilspill = Hazards(1000, 680, 5, oilspill_img, "bloodspill")
    beartrap = Hazards(1200, 608, 5, beartrap_img, "beartrap")
    hazard_sign = Hazards(1500, 760, 5, roadsign_img, "hazard_sign")
    all_hazards = pygame.sprite.Group()
    all_hazards.add(oilspill)
    all_hazards.add(beartrap)
    all_hazards.add(hazard_sign)

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
                    sys.exit() #TODO exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill((0, 0, 0))
                        loop = False
            pygame.display.update()
            clock.tick(60)

    def display_score():
        current_score = playerCar.score
        score_surface = corbelfont.render(f" Score:{current_score}", False, (197, 136, 215))
        score_rect = score_surface.get_rect(center=(400, 30))
        screen.blit(score_surface, score_rect)

    def check_collisions(playerCar, all_hazards): # TODO redo
        tester = ""
        for sprite in all_hazards:
            if pygame.sprite.collide_mask(playerCar, sprite) is None:
                pass
            else:
                tester = sprite.getType()
                print(tester)
        return tester

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

            # collision logic

            if check_collisions(playerCar, all_hazards) == "bloodspill":
                playerCar.change_rand_lane()
            elif check_collisions(playerCar, all_hazards) == "beartrap":
                if playerCar.get_damaged(5):
                    game_active = False
                else:
                    pygame.time.delay(5000)
                    healthbar.hp = playerCar.health
                    beartrap.rect.center = [1400, random.choice([605, 682, 760])]
            elif check_collisions(playerCar, all_hazards) == "hazard_sign":
                if playerCar.get_damaged(5):
                    game_active = False
                else:
                    healthbar.hp = playerCar.health
                    hazard_sign.rect.center = [1400, random.choice([605, 682, 760])]
            # test position
            # print(playerCar.rect.x)
            # print(playerCar.rect.y)

            # actually its 1000 but testing 200
            if playerCar.score == 400:
                # scuffed
                from garage import garage_screen
                garage_screen(playerCar, healthbar, 2)
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
    sys.exit() #TODO exit
