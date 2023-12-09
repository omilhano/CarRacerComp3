import pygame
import hazards
import random
from config import normal_car


class Car(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    # Initialize constants
    # todo required python
    TOP_LANE_Y = 480
    MID_LANE_Y = 555
    BOTTOM_LANE_Y = 630

    def __init__(self, position_x, position_y, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the car image
        self.image = pygame.image.load(normal_car).convert_alpha()
        self.rect = self.image.get_rect()
        self.car_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
        self.speed = speed
        self.health = 100
        self.max_hp = self.health
        self.score = 0
        self.money = 0

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

    def collide_beartrap(self):  # TODO
        # using pygame.time.get_ticks()
        # make so that no key pressed works
        # called inside the levels code
        pass

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.right > 1270:
            self.rect.x -= pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x += pixels

    def moveUp(self):
        if self.rect.y == Car.MID_LANE_Y:
            self.rect.y = Car.TOP_LANE_Y
        elif self.rect.y == Car.BOTTOM_LANE_Y:
            self.rect.y = Car.MID_LANE_Y

    def moveDown(self):
        if self.rect.y == Car.TOP_LANE_Y:
            self.rect.y = Car.MID_LANE_Y
        elif self.rect.y == Car.MID_LANE_Y:
            self.rect.y = Car.BOTTOM_LANE_Y

    def changeSpeed(self, speed):
        self.speed = speed

    def get_money(self, zombie) -> None:
        self.money += zombie.money
        zombie.zombie_tp()

    def updateScore(self, score):
        self.score += score

    def change_rand_lane(self):
        if self.rect.y == Car.TOP_LANE_Y:
            self.rect.y = random.choice([Car.MID_LANE_Y, Car.BOTTOM_LANE_Y])
        elif self.rect.y == Car.MID_LANE_Y:
            self.rect.y = random.choice([Car.TOP_LANE_Y, Car.BOTTOM_LANE_Y])
        else:
            self.rect.y = random.choice([Car.TOP_LANE_Y, Car.MID_LANE_Y])
