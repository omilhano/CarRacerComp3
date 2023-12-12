import time

import pygame
import hazards
import random
from config import normal_car
from powerUps import Invincible


class Car(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    # Initialize constants
    # todo required python
    # TODO screen auto adjust
    TOP_LANE_Y = 480
    MID_LANE_Y = 555
    BOTTOM_LANE_Y = 630

    def __init__(self, position_x, position_y, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the car image

        self.can_collide = True
        self.image = pygame.image.load(normal_car).convert_alpha()
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

    # If collide lower hp
    # Returns true if kill car
    def get_damaged(self, hazard) -> bool:
        if hazard.get_type() == "spill":
            self.collide_spill()
        if hazard.get_type() == "beartrap":
            self.collide_beartrap()
        self.health -= hazard.get_damage()
        hazard.hazard_tp()
        return self.health <= 0

    def gain_powerup(self, powerup):
        if isinstance(powerup, Invincible):
            self.gain_invincibility()
        powerup.powerup_tp()

    def gain_invincibility(self):  # TODO change car appearance
        if self.can_collide:
            self.can_collide = False
            self.status_change_time = time.time()

    def update_powerup(self):
        if not self.can_collide and time.time() > self.status_change_time + 5:
            self.can_collide = True

    def collide_spill(self):
        self.change_rand_lane()

    def collide_beartrap(self):  # TODO change car appearance
        if self.movement:
            self.movement = False
            self.status_change_time = time.time()

    def update_movement(self):
        if not self.movement and time.time() > self.status_change_time + 5:
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
            if self.rect.y == Car.MID_LANE_Y:
                self.rect.y = Car.TOP_LANE_Y
            elif self.rect.y == Car.BOTTOM_LANE_Y:
                self.rect.y = Car.MID_LANE_Y

    def moveDown(self):
        if self.movement:
            if self.rect.y == Car.TOP_LANE_Y:
                self.rect.y = Car.MID_LANE_Y
            elif self.rect.y == Car.MID_LANE_Y:
                self.rect.y = Car.BOTTOM_LANE_Y

    def changeSpeed(self, speed):
        self.speed = speed

    def get_money(self, zombie) -> None:
        self.money += zombie.money
        zombie.zombie_tp()

    def updateScore(self, hazard_type):
        self.score += hazards.hazard_types[hazard_type]["score"]

    def change_rand_lane(self):
        if self.rect.y == Car.TOP_LANE_Y:
            self.rect.y = random.choice([Car.MID_LANE_Y, Car.BOTTOM_LANE_Y])
        elif self.rect.y == Car.MID_LANE_Y:
            self.rect.y = random.choice([Car.TOP_LANE_Y, Car.BOTTOM_LANE_Y])
        else:
            self.rect.y = random.choice([Car.TOP_LANE_Y, Car.MID_LANE_Y])
