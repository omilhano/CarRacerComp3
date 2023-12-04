import pygame
import healthbar
import random


class Car(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    # Initialize constants
    #  why doesnt it work liah :3
    #does it need to be inside innit
    TOP_LANE_Y = 480
    MID_LANE_Y = 555
    BOTTOM_LANE_Y = 630
    def __init__(self, position_x, position_y, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the car image
        self.image = pygame.image.load("images/pickup_test.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.car_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
        self.speed = speed
        self.health = 100
        self.max_hp = self.health
        self.score = 0

    def get_damaged(self, damage):
        # If collide lower hp
        # Returns true if kill car
        self.health -= damage
        return self.health <= 0

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def objectSpeed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def moveUp(self):
        if self.rect.y == 555:
            self.rect.y = 480
        elif self.rect.y == 630:
            self.rect.y = 555

    def moveDown(self):
        if self.rect.y == 480:
            self.rect.y = 555
        elif self.rect.y == 555:
            self.rect.y = 630

    def changeSpeed(self, speed):
        self.speed = speed

    def updateScore(self, score):
        self.score += score

    def change_rand_lane(self):
        if self.rect.y == 480:
            self.rect.y = random.choice([555, 630])
        elif self.rect.y == 555:
            self.rect.y = random.choice([480, 630])
        else:
            self.rect.y = random.choice([480, 555])
