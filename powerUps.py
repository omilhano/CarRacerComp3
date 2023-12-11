import random
import pygame
from abc import ABC
from config import invincibility


class Powers(ABC, pygame.sprite.Sprite):

    def __init__(self, position_x, position_y, speed, type, probability):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.probability = probability
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.type = type

    def can_spawn(self) -> bool:
        var_rand = random.random()
        # true if spawn
        return var_rand <= self.probability

    # @abstractmethod
    # def getType(self):
    #     return self.type


# TODO this
class Invincible(Powers):
    def __init__(self, position_x, position_y, ):
        super().__init__(position_x, position_y, 9, "invincible", 0.0004)  # todo change probability and size

        self.image = pygame.image.load(invincibility).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]

    def powerup_tp(self) -> None:
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20

    # invincible make car take no damage
    # how to implement this? remove collision?
