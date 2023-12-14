import random
import time

import pygame
from abc import ABC, abstractmethod

from config import invincibility, bear_trap, invincible_car, normal_car, spill_car, slow


class PowerUp(ABC, pygame.sprite.Sprite):

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

    @abstractmethod
    def powerup_tp(self) -> None:
        pass

    @abstractmethod
    def affect_player(self, player):
        pass

    @abstractmethod
    def affect_traffic(self):
        pass


class Invincible(PowerUp):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "invincible", 0.0005)

        self.image = pygame.image.load(invincibility).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]

    # overriding abstract method
    def affect_player(self, player):
        if player.can_collide:
            player.image = pygame.image.load(invincible_car).convert_alpha()
            player.can_collide = False
            player.status_change_time = time.time()
            self.powerup_tp()

    def powerup_tp(self) -> None:
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def affect_traffic(self):
        pass


class BearTrap(PowerUp):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "beartrap", 0.002)

        self.image = pygame.image.load(bear_trap).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
        self.damage = 3
        self.score = 25

    def affect_player(self, player):
        if player.movement:
            player.image = pygame.image.load(spill_car).convert_alpha()
            player.movement = False
            player.status_change_time = time.time()
            player.health -= self.get_damage()
            self.powerup_tp()

    def powerup_tp(self) -> None:
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def affect_traffic(self):
        pass

    def get_damage(self):
        return self.damage

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20


class SlowTime(PowerUp):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "slow_time", 0.002)
        self.image = pygame.image.load(slow).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]

    def powerup_tp(self) -> None:
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def affect_traffic(self):
        hazards.status_change_time = time.time()
        self.powerup_tp()
        pass

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def affect_player(self, player):
        pass
