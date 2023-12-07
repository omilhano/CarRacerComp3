from turtle import speed

import pygame
from abc import ABC, abstractmethod

from config import invincibility


class Powers(ABC, pygame.sprite.Sprite):

    def __init__(self, position_x, position_y, speed, type):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.type = type

    # def object_speed(self, speed):
    #     self.rect.x -= self.speed * speed / 20

    # @abstractmethod
    # def getType(self):
    #     return self.type

#TODO this
class Invincible(Powers):
    def __init__(self, position_x, position_y, ):
        super().__init__(position_x, position_y, 9, "invincible")

        self.image = pygame.image.load(invincibility).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
    # invincible make car take no damage
    # how to implement this? remove collision?
