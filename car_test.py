import pygame


class Car(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self,position_x, position_y, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the car image
        self.image = pygame.image.load("images/pickup_test.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.car_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
        self.speed = speed



    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def objectSpeed(self, speed):
        self.rect.x -= self.speed * speed / 20

    def moveForward(self, pixels):
        self.rect.y += pixels

    def moveBackward(self, pixels):
        self.rect.y -= pixels

    def changeSpeed(self, speed):
        self.speed = speed

