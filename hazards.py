import pygame


class Hazards(pygame.sprite.Sprite):

    def __init__(self, position_x, position_y, speed, health):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("images/oil_spill.png").convert_alpha()