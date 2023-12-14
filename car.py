import time

import pygame
import hazards
import random
from config import normal_car, invincible_car, spill_car, normal_bike
from powerUps import Invincible


class Car(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    # Initialize constants
    # TODO screen auto adjust

    def __init__(self, position_x, position_y, speed, vehicle_type):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the car image

        self.can_collide = True
        self.vehicle_type = vehicle_type
        self.image = pygame.image.load(vehicles[vehicle_type]["image"]).convert_alpha()
        self.rect = self.image.get_rect()
        self.car_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
        self.speed = speed
        self.health = 100
        self.max_hp = self.health
        self.score = 0
        self.money = 0
        self.movement = True
        self.status_change_time = 0
        self.top_lane = vehicles[vehicle_type]["top"]
        self.mid_lane = vehicles[vehicle_type]["mid"]
        self.bottom_lane = vehicles[vehicle_type]["bottom"]

    # If collide lower hp
    # Returns true if kill car
    def get_damaged(self, hazard) -> bool:
        if hazard.get_type() == "spill":
            self.collide_spill()
        self.health -= hazard.get_damage()
        hazard.hazard_tp()
        return self.health <= 0

    def collide_spill(self):
        self.change_rand_lane()

    def update_powerup(self):
        if not self.can_collide and time.time() > self.status_change_time + 5:
            self.image = pygame.image.load(normal_car).convert_alpha()
            self.can_collide = True

    def update_movement(self):
        if not self.movement and time.time() > self.status_change_time + 5:
            self.image = pygame.image.load(normal_car).convert_alpha()
            self.movement = True

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.movement:
            if self.rect.right > 1270:
                self.rect.x -= pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.movement:
            if self.rect.x < 0:
                self.rect.x += pixels

    def moveUp(self):
        if self.movement:
            if self.rect.y == self.mid_lane:
                self.rect.y = self.top_lane
            elif self.rect.y == self.bottom_lane:
                self.rect.y = self.mid_lane

    def moveDown(self):
        if self.movement:
            if self.rect.y == self.top_lane:
                self.rect.y = self.mid_lane
            elif self.rect.y == self.mid_lane:
                self.rect.y = self.bottom_lane

    def changeSpeed(self, speed):
        self.speed = speed

    def get_money(self, zombie) -> None:
        self.money += zombie.money
        zombie.zombie_tp()

    def updateScore(self, hazard_type):
        self.score += hazards.hazard_types[hazard_type]["score"]

    def change_rand_lane(self):
        if self.rect.y == self.top_lane:
            self.rect.y = random.choice([self.mid_lane, self.bottom_lane])
        elif self.rect.y == self.mid_lane:
            self.rect.y = random.choice([self.top_lane, self.bottom_lane])
        else:
            self.rect.y = random.choice([self.top_lane, self.mid_lane])


vehicles = {
    "bike": {"image": normal_bike, "top": 505, "mid": 580, "bottom": 650},

    "car": {"image": normal_car, "top": 480, "mid": 555, "bottom": 630}
}
