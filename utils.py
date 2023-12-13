import sys

import pygame

from config import pause_menu, level1_end
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


end_screens = {
    1: {"image": level1_end},

    2: {"image": pause_menu},

    3: {"image": pause_menu}
}
