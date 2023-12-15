import time
import pygame
import hazards
import random
from config import normal_car, normal_bike


class Car(pygame.sprite.Sprite):
    """
        A class that represents the player
        ...

        Attributes

        ----------
        vehicle_type : str
            either "car" or "bike", used to identify the sprite used for the player
        top_lane : int
            the y value corresponding to the top lane
        mid_lane : int
            the y value corresponding to the mid lane
        bottom_lane : int
            the y value corresponding to the bottom lane
        image : Surface
            sprite of the vehicle
        rect : Rect
            creates a rectangle around the image
        car_mask : Mask
            creates a mask from the image
        rect.center : tuple
            sets the center of the rectangle at those coordinates
        health : int
            the health of the player
        score : int
            the score of the player
        money : int
            the money of the player
        status_change_time : int
            #TODO alex what is this
        can_move : bool
            to check if the player can move
        can_collide : bool
            to check if the player can collide with other objects
        time_slowed : bool
            to check if the time is slowed

        Methods
        -------
        get_damaged(hazard):
            Affects the player when it hits a hazard
        collide_spill():
            Teleports the player to a random lane
        update_powerup():
            reverts the positive powerup Invincibility effect
        update_movement():
            reverts the negative powerup Beartrap effect
        move_right():
            moves the sprite 5 pixels to the right
        move_left():
            moves the sprite 5 pixels to the right
        move_up():
            moves the sprite up one lane
            doesn't do anything if the player is already in the top most lane
        move_down():
            moves the sprite down one lane
            doesn't do anything if the player is already in the bottom most lane
        get_money(zombie)
            Affects the player when it hits a zombie
        update_score(hazard_type)
            Updates the score of the player
        change_rand_lane():
            Teleports the player to a random lane
        """

    def __init__(self, vehicle_type):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.vehicle_type = vehicle_type
        self.top_lane = vehicles[self.vehicle_type]["top"]
        self.mid_lane = vehicles[self.vehicle_type]["mid"]
        self.bottom_lane = vehicles[self.vehicle_type]["bottom"]
        self.image = pygame.image.load(vehicles[vehicle_type]["image"]).convert_alpha()
        self.rect = self.image.get_rect()
        self.car_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [130, 680]
        self.health = 100
        self.score = 0
        self.money = 0
        self.status_change_time = 0
        self.can_move = True
        self.can_collide = True
        self.time_slowed = False

    def get_damaged(self, hazard) -> bool:
        """
        Applies effects to player when it hits the hazard.
        If the hazard is of type "Spill" calls collide_spill function.
        Removes health from the player equal to the damage value of the hazard
        Returns true if after getting damaged, the player's health is equal to or below 0

        :param hazard: object from class Hazard
        :return: true if player health is below or equal to 0
        """
        if hazard.get_type() == "spill":
            self.collide_spill()
        self.health -= hazard.get_damage()
        hazard.hazard_tp()
        return self.health <= 0

    def collide_spill(self):
        """
        Calls a function to teleport the player
        :return: None
        """
        self.change_rand_lane()

    def update_powerup(self):
        """
        Checks to see if player cannot collide and
        Checks if 5 seconds have passed since the player
        collided with the powerup Invincibility
        If true, reverts the Car sprite to its original and
        the car is allowed to collide again


        :return: None
        """
        if not self.can_collide and time.time() > self.status_change_time + 5:
            self.image = pygame.image.load(vehicles[self.vehicle_type]["image"]).convert_alpha()
            self.can_collide = True

    def update_movement(self):
        """
        Checks if player cannot move and
        Checks if 5 seconds have passed since the player
        collided with the powerup Beartrap
        If true, reverts the Car sprite to its original
        and the car is allowed to move again

        :return: None
        """
        if not self.can_move and time.time() > self.status_change_time + 5:
            self.image = pygame.image.load(vehicles[self.vehicle_type]["image"]).convert_alpha()
            self.can_move = True

    def move_right(self):
        """
        Checks to see if player is allowed to move
        Moves the player 5 pixels to the right
        Checks to see if player is to the right of the screen limit
        If that's the case, moves the player 5 pixels to the left

        :return: None
        """
        if self.can_move:
            self.rect.x += 5
            if self.rect.right > 1270:
                self.rect.x -= 5

    def move_left(self):
        """
        Checks to see if player is allowed to move
        Moves the player 5 pixels to the left
        Checks to see if player is to the left of the screen limit
        If that's the case, moves the player 5 pixels to the right

        :return: None
        """
        if self.can_move:
            self.rect.x -= 5
            if self.rect.x < 0:
                self.rect.x += 5

    def move_up(self):
        """
        Checks to see if player is allowed to move
        Checks to see if player is in the middle lane
        If so, teleports player to top lane
        Checks to see if player is in the bottom lane
        If so, teleports player to middle lane

        :return: None
        """
        if self.can_move:
            if self.rect.y == self.mid_lane:
                self.rect.y = self.top_lane
            elif self.rect.y == self.bottom_lane:
                self.rect.y = self.mid_lane

    def move_down(self):
        """
        Checks to see if player is allowed to move
        Checks to see if player is in the top lane
        If so, teleports player to middle lane
        Checks to see if player is in the middle lane
        If so, teleports player to bottom lane

        :return: None
        """
        if self.can_move:
            if self.rect.y == self.top_lane:
                self.rect.y = self.mid_lane
            elif self.rect.y == self.mid_lane:
                self.rect.y = self.bottom_lane

    def get_money(self, zombie) -> None:
        """
        Adds money to the player equal to the money value of the zombie
        Teleports zombie outside the screen region
        :param zombie: object from the class Zombies
        :return: None
        """
        self.money += zombie.get_money()
        zombie.zombie_tp()

    def update_score(self, hazard):
        """
        Adds score to the player equal to the score value of the hazard

        :param hazard: object from class Hazards
        :return: None
        """
        self.score += hazard.get_score()

    def change_rand_lane(self):
        """
        Checks to see if player is in the top lane
        If so, teleports player to either the middle lane or the bottom lane, at random
        Checks to see if player is in the middle lane
        If so, teleports player to either the top lane or the bottom lane, at random
        Otherwise, teleports player to either the top lane or the middle lane, at random

        :return: None
        """
        if self.rect.y == self.top_lane:
            self.rect.y = random.choice([self.mid_lane, self.bottom_lane])
        elif self.rect.y == self.mid_lane:
            self.rect.y = random.choice([self.top_lane, self.bottom_lane])
        else:
            self.rect.y = random.choice([self.top_lane, self.mid_lane])


"""
Dictionary containing the information related to the two types of sprites an object from this class
can take
image: the sprite of a car or a bike
top: the y value corresponding to the best value for the sprite to appear in the top lane
mid: the y value corresponding to the best value for the sprite to appear in the middle lane
bottom: the y value corresponding to the best value for the sprite to appear in the bottom lane
"""
vehicles = {
    "bike": {"image": normal_bike, "top": 505, "mid": 580, "bottom": 650},

    "car": {"image": normal_car, "top": 480, "mid": 555, "bottom": 630}
}
