import random
import pygame
from config import road_sign_lv1, cone, blood_spill


class Hazards(pygame.sprite.Sprite):
    """
        A class that represents the hazards
        ...

        Attributes
        hazard_type : str
            either "tall", "small" or "spill" used to attribute correct values to different types
            of hazard using the hazard_types dictionary
        position_x : int
            value of the x coordinate where the hazard spawns
        position_y : int
            value of the y coordinate where the hazard spawns
        speed: int
            speed at which the hazard moves
        damage : int
            damage the hazard gives the player
        score: int
            score which the hazard gives, after passing the left of the screen
        image : Surface
            sprite of the hazard
        rect : Rect
            creates a rectangle around the image
        rect.center : tuple
            sets the center of the rectangle at those coordinates
        hazard_mask : Mask
            creates a mask from the image
        ----------
        Methods
            update():
                updates the position of the cursor to the position of the mouse
        -------
        """

    def __init__(self, hazard_type, position_x, position_y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.hazard_type = hazard_type
        self.position_x = position_x
        self.position_y = position_y
        self.speed = 5

        # options for hazards
        self.damage = hazard_types[hazard_type]["damage"]
        self.score = hazard_types[hazard_type]["score"]
        self.image = pygame.image.load(hazard_types[hazard_type]["image"]).convert_alpha()

        # Defining rectangle and positions
        self.rect = self.image.get_rect()
        self.rect.center = [self.position_x, self.position_y]
        self.hazard_mask = pygame.mask.from_surface(self.image)

    def object_speed(self, speed):
        """
        Functions that dictates how fast
        the objects move to the left of the screen
        :param speed: int 
        :return: None
        """
        self.rect.x -= self.speed * speed / 20

    def get_score(self):
        """
        :return: score
        """
        return self.score

    def get_type(self):
        """
        :return: type of hazard
        """
        return self.hazard_type

    def get_damage(self):
        """
        :return: damage
        """
        return self.damage

    def hazard_tp(self):
        """
        Teleports hazard to outside the screen region at a random x coordinate and
        at one of the lanes at random
        :return: None
        """
        self.rect.center = [random.randint(1300, 1400), random.choice([605, 682, 760])]

    def return_normal(self):
        """
        Returns both the sprite and the speed to normal
        Used to return the hazard back to normal after the slow power up
        :return: None
        """
        self.image = pygame.image.load(hazard_types[self.hazard_type]["image"]).convert_alpha()
        self.speed = 5


"""
Dictionary containing the information related to the three types an object from this class
can be
damage: the amount of damage the specific hazard gives
image: the sprite of the different hazards
score: the score the hazard give as it exits the screen
Ready for future implementation
"""
hazard_types = {
    "tall": {"damage": 5, "image": road_sign_lv1, "score": 100},

    "small": {"damage": 3, "image": cone, "score": 25},

    "spill": {"damage": 0, "image": blood_spill, "score": 75}

    # "oilspill": {"damage": 0, "image": oil_spill, "score": 75}
}
