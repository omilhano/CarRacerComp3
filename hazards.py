import random
import pygame
from config import road_sign_lv1, cone, blood_spill, oil_spill


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
        self.score = hazard_types[hazard_type]["score"]
        self.image = pygame.image.load(hazard_types[hazard_type]["image"]).convert_alpha()

        # Defining rectangle and positions
        self.rect = self.image.get_rect()
        self.rect.center = [self.position_x, self.position_y]
        self.hazard_mask = pygame.mask.from_surface(self.image)

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def get_score(self):
        return self.score

    def get_type(self):
        return self.hazard_type

    def get_damage(self):
        return self.damage

    def hazard_tp(self):
        self.rect.center = [random.randint(1300, 1400), random.choice([605, 682, 760])]

    def return_normal(self):
        self.image = pygame.image.load(hazard_types[self.hazard_type]["image"]).convert_alpha()
        self.speed = 5


hazard_types = {
    "tall": {"damage": 5, "image": road_sign_lv1, "score": 100},

    "small": {"damage": 3, "image": cone, "score": 25},

    "spill": {"damage": 0, "image": blood_spill, "score": 75},

    "oilspill": {"damage": 0, "image": oil_spill, "score": 75}
}
