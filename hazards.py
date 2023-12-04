import pygame
# TODO change ammount of damage each hazard gives
# TODO theyre still spawning on top of each other respectfully
# TODO change amount of score each hazard gives
# TODO oilspill creative for powerup
class Hazards(pygame.sprite.Sprite):

    def __init__(self, position_x, position_y, speed, path_file, type):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = path_file
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.position_x = position_x
        self.position_y = position_y
        self.rect.center = [position_x, position_y]
        self.speed = speed
        self.type = type


    def getType(self):
        return self.type
