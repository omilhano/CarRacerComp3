import pygame
import random
from config import normal_zombie, fast_zombie, static_zombie


# Todo make fast zombie even more rare
class Zombies(pygame.sprite.Sprite):
    def __init__(self, type_zombie, position_x, position_y):
        super().__init__()

        self.position_x = position_x
        self.position_y = position_y
        self.type_zombie = type_zombie

        # options for the zombies
        self.speed = zombie_types[type_zombie]["speed"]
        self.money = zombie_types[type_zombie]["money"]
        self.probability = zombie_types[type_zombie]["probability"]
        self.image = pygame.image.load(zombie_types[type_zombie]["image"]).convert_alpha()

        # Defining rectangle and positions
        self.rect = self.image.get_rect()
        self.rect.center = [self.position_x, self.position_y]
        self.zombie_mask = pygame.mask.from_surface(self.image)

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def can_spawn(self) -> bool:
        var_rand = random.random()
        # true if spawn
        return var_rand <= self.probability


zombie_types = {
    "fast": {"speed": 10, "money": 5, "probability": 0.0005, "image": fast_zombie},

    "normal": {"speed": 6.5, "money": 3, "probability": 0.001,
               "image": normal_zombie},

    "static": {"speed": 5, "money": 1, "probability": 0.007, "image": static_zombie}
}
