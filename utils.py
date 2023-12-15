import sys
import pygame
from config import pause_menu, level1_end, no_save
from garage import garage_screen

pygame.init()

# defining screen
res = (1282, 800)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Car Racing")
# font
corbelfont = pygame.font.SysFont('Corbel', 50)  # Select font and size
clock = pygame.time.Clock()


def pause():
    loop = True
    pause_screen = pygame.image.load(pause_menu).convert_alpha()
    screen.blit(pause_screen, [0, 0])
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


def level_end(level, playerCar, healthbar):
    loop = True
    end_screen = pygame.image.load(end_screens[level]["image"]).convert_alpha()
    screen.blit(end_screen, [0, 0])
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                garage_screen(playerCar, healthbar, 1)
        pygame.display.update()


def no_save_file():
    loop = True
    end_screen = pygame.image.load(no_save).convert_alpha()
    screen.blit(end_screen, [0, 0])
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                from mainmenu import menu
                menu()
        pygame.display.update()


end_screens = {
    1: {"image": level1_end},

    # 2: {"image": level2_end},
    #
    # 3: {"image": level3_end}
}
