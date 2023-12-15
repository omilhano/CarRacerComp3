import pygame
import random
from config import normal_zombie, fast_zombie, static_zombie


class Zombies(pygame.sprite.Sprite):
    """
        A class that represents the zombies
        ...

        Attributes
        hazard_type : str
            either "tall", "small" or "spill" used to attribute correct values to different types
            of hazard using the zombie_types dictionary
        position_x : int
            value of the x coordinate where the zombie spawns
        position_y : int
            value of the y coordinate where the zombie spawns
        speed: int
            speed at which the zombie moves
        money : int
            money the zombie gives the player
        probability: int
            probability of zombie appearing on screen
        image : Surface
            sprite of the zombie
        rect : Rect
            creates a rectangle around the image
        rect.center : tuple
            sets the center of the rectangle at those coordinates
        zombie_mask : Mask
            creates a mask from the image
        ----------
        Methods
            get_money():
                gives player money
            can_spawn():

        -------
        """

    def __init__(self, type_zombie, position_x, position_y):
        super().__init__()

        self.position_x = position_x
        self.position_y = position_y
        self.type_zombie = type_zombie

        # options for the zombies
        self.speed = zombie_types[type_zombie]["speed"]
        self.money = zombie_types[type_zombie]["money"]
        self.probability = zombie_types[type_zombie]["probability"]
        self.image = pygame.image.load(zombie_types[type_zombie]["image"]).convert_alpha()

        # Defining rectangle and positions
        self.rect = self.image.get_rect()
        self.rect.center = [self.position_x, self.position_y]
        self.zombie_mask = pygame.mask.from_surface(self.image)

    def object_speed(self, speed):
        """

        :param speed: int speed objects move to left of the screen
        :return: None
        """
        self.rect.x -= self.speed * speed / 20

    def get_money(self):
        """
        :return: money
        """
        return self.money

    def can_spawn(self) -> bool:
        """
        :return: bool if it can spawn
        """
        var_rand = random.random()
        # true if spawn
        return var_rand <= self.probability

    def zombie_tp(self) -> None:
        """
        Checks if zombie can spawn
        If True, allocates to a random lane off screen
        If False, puts them on a coordinates that forces a spawn
        :return: None
        """
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def return_normal(self):
        """
        Reverts the changes from the power
        Changes speed to normal and image to normal
        :return: None
        """
        self.speed = zombie_types[self.type_zombie]["speed"]
        self.image = pygame.image.load(zombie_types[self.type_zombie]["image"]).convert_alpha()


"""
Dictionary containing the information related to the three types an object from this class
can be
speed: speed at which they move to the left of screen
image: the sprite of the different zombies
money: the money the zombie give as it exits the screen
Ready for future implementation
"""
zombie_types = {
    "fast": {"speed": 10, "money": 5, "probability": 0.0005, "image": fast_zombie},

    "normal": {"speed": 6.5, "money": 3, "probability": 0.001,
               "image": normal_zombie},

    "static": {"speed": 5, "money": 1, "probability": 0.007, "image": static_zombie}
}
