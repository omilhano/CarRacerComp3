import pygame
import healthbar

class Car(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self,position_x, position_y, speed, health):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the car image
        self.image = pygame.image.load("images/pickup_test.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.car_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
        self.speed = speed
        self.health = health

    # TODO ask if healthbar should be in menu or in car or should be two separate identities
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
