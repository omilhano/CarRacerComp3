import pygame


class Hazards(pygame.sprite.Sprite):

    def __init__(self, position_x, position_y, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("images/oil_spill.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.car_mask = pygame.mask.from_surface(self.image)
        self.position_x = position_x
        self.position_y = position_y
        self.rect.center = [position_x, position_y]
        self.speed = speed


    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20
