import pygame
import random


class Zombies(pygame.sprite.Sprite):
    def __init__(self, type_zombie, position_x, position_y):
        super().__init__()

        self.probability = 0
        self.position_x = position_x
        self.position_y = position_y
        self.type_zombie = type_zombie
        self.speed = 0
        self.money = 0
        self.zombie_mask = None
        self.rect = None
        self.image = None

    def assign_attributes(self):
        if self.type_zombie == "fast":
            self.image = pygame.image.load("images/fastZombie.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [self.position_x, self.position_y]
            self.zombie_mask = pygame.mask.from_surface(self.image)
            self.speed = 10
            self.money = 5
            self.probability = 0.9995
        elif self.type_zombie == "static":
            self.image = pygame.image.load("images/staticZombie.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [self.position_x, self.position_y]
            self.zombie_mask = pygame.mask.from_surface(self.image)
            self.speed = 5
            self.money = 1
            self.probability = 0.993
        else:
            self.image = pygame.image.load("images/zombie.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = [self.position_x, self.position_y]
            self.zombie_mask = pygame.mask.from_surface(self.image)
            self.speed = 6.5
            self.money = 3
            self.probability = 0.999

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def can_spawn(self):
        var_rand = random.random()
        # true if spawn
        return var_rand >= self.probability