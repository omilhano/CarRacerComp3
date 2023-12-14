import random
import time

import pygame
from abc import ABC, abstractmethod

from config import invincibility, bear_trap, invincible_car, slow, fast_zombieBW, normal_zombieBW, \
    static_zombieBW, road_sign_lv1BW, blood_spillBW, invincibilityBW, slowBW, bear_trapBW, invincible_bike, stuck_car, \
    stuck_bike


class PowerUp(ABC, pygame.sprite.Sprite):

    def __init__(self, position_x, position_y, speed, power_up_type, probability):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.probability = probability
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.type = power_up_type

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
    def affect_traffic(self, zombies, traffic, powers):
        pass

    @abstractmethod
    def return_normal(self):
        pass


class Invincible(PowerUp):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "invincible", 0.0005)

        self.power_up_type = "invincible"  # Test
        self.image = pygame.image.load(invincibility).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]

    # overriding abstract method
    def affect_player(self, player):
        if player.can_collide:
            player.image = pygame.image.load(invincibility_vehicles[player.vehicle_type]["invincible"]).convert_alpha()
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

    def affect_traffic(self, zombies, traffic, powers):
        pass

    def return_normal(self):
        self.speed = 9
        self.image = pygame.image.load(invincibility).convert_alpha()


invincibility_vehicles = {
    "car": {"bear_trap": stuck_car, "invincible": invincible_car},

    "bike": {"bear_trap": stuck_bike, "invincible": invincible_bike}
}


class BearTrap(PowerUp):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "beartrap", 0.002)

        self.power_up_type = "beartrap"  # Test
        self.image = pygame.image.load(bear_trap).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
        self.damage = 3
        self.score = 25

    def affect_player(self, player):
        if player.movement:
            player.image = pygame.image.load(stuck_car).convert_alpha()
            player.movement = False
            player.status_change_time = time.time()
            player.health -= self.get_damage()
            self.powerup_tp()

    def powerup_tp(self) -> None:
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def affect_traffic(self, zombies, traffic, powers):
        pass

    def return_normal(self):
        self.speed = 9
        self.image = pygame.image.load(bear_trap).convert_alpha()

    def get_damage(self):
        return self.damage

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20


class SlowTime(PowerUp):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "slow_time", 0.002)
        self.power_up_type = "slow_time"  # Test
        self.image = pygame.image.load(slow).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]

    def powerup_tp(self) -> None:
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def affect_traffic(self, zombies, traffic, powers):
        for zombie in zombies:
            zombie.speed -= 4
            zombie.image = pygame.image.load(slowed_sprites[zombie.type_zombie]["bw_sprite"]).convert_alpha()
        for hazard in traffic:
            hazard.speed = 1
            hazard.image = pygame.image.load(slowed_sprites[hazard.hazard_type]["bw_sprite"]).convert_alpha()
        for power in powers:
            power.speed = 5
            power.image = pygame.image.load(slowed_sprites[power.power_up_type]["bw_sprite"]).convert_alpha()
        self.powerup_tp()

    def object_speed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def affect_player(self, player):
        pass

    def return_normal(self):
        self.speed = 9
        self.image = pygame.image.load(slow).convert_alpha()


slowed_sprites = {
    "fast": {"bw_sprite": fast_zombieBW},

    "normal": {"bw_sprite": normal_zombieBW},

    "static": {"bw_sprite": static_zombieBW},

    "spill": {"bw_sprite": blood_spillBW},

    "tall": {"bw_sprite": road_sign_lv1BW},

    "invincible": {"bw_sprite": invincibilityBW},

    "slow_time": {"bw_sprite": slowBW},

    "beartrap": {"bw_sprite": bear_trapBW}
}
