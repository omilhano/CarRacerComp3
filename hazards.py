import random

import pygame

from config import road_sign_lv1, cone, blood_spill


# TODO theyre still spawning on top of each other respectfully
# TODO change amount of score each hazard gives !!!
# TODO oilspill creative for powerup
# TODO class child
class Hazards(pygame.sprite.Sprite):

    def __init__(self, hazard_type, position_x, position_y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.hazard_type = hazard_type
        self.position_x = position_x
        self.position_y = position_y
        self.speed = 5
        # options for hazards
        self.damage = hazard_types[hazard_type]["damage"]
        self.image = pygame.image.load(hazard_types[hazard_type]["image"]).convert_alpha()

        # Defining rectangle and positions
        self.rect = self.image.get_rect()
        self.rect.center = [self.position_x, self.position_y]
        self.hazard_mask = pygame.mask.from_surface(self.image)

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def get_type(self):  # liahhhh
        return self.hazard_type

    def get_damage(self):
        return self.damage

    def hazard_tp(self):
        self.rect.center = [1400, random.choice([605, 682, 760])]


hazard_types = {
    "tall": {"damage": 5, "image": road_sign_lv1},

    "small": {"damage": 3, "image": cone},

    "spill": {"damage": 0, "image": blood_spill}
}
