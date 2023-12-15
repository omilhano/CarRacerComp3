import random
import time
import pygame
from abc import ABC, abstractmethod
from config import invincibility, bear_trap, invincible_car, slow, fast_zombieBW, normal_zombieBW, \
    static_zombieBW, road_sign_lv1BW, blood_spillBW, invincibilityBW, slowBW, bear_trapBW, invincible_bike, stuck_car, \
    stuck_bike


class PowerUp(ABC, pygame.sprite.Sprite):
    """
        A class that represents power ups
        ...

        Attributes
        probability : int
            probability of power up spawning
        position_x : int
            value of the x coordinate where the power up spawns
        position_y : int
            value of the y coordinate where the power up spawns
        speed : int
            speed at which the power up moves
        type : str
            either "invincible", "slow_time" or "beartrap" used to attribute correct sprite for the slow visual effect
            using the slowed_sprites dictionary
        ----------
        Methods
            can_spawn():
                Used to attribute rarity to the power ups
        -------
        """
    def __init__(self, position_x, position_y, speed, power_up_type, probability):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.probability = probability
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.type = power_up_type

    def can_spawn(self) -> bool:
        """
        Creates a random variable between 0 and 1
        :return: True if the variable is smaller than the probability, the power up can spawn
        """
        var_rand = random.random()
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
    """
        A class that represents the invincibility power up
        ...
        Attributes
        probability : int
            probability of power up spawning, 0.0005
        position_x : int
            value of the x coordinate where the power up spawns
        position_y : int
            value of the y coordinate where the power up spawns
        speed : int
            speed at which the power up moves
        type : str
            "invincible"used to attribute correct sprite for the slow visual effect
            using the slowed_sprites dictionary
        image : Surface
            sprite of the invincible power up
        rect : Rect
            creates a rectangle around the image
        rect.center : tuple
            sets the center of the rectangle at those coordinates
        hazard_mask : Mask
            creates a mask from the image
        ----------
        Methods
            affect_player(player) :
                puts the player under the affect of the power up
            powerup_tp() :
                teleports power up
            object_speed(speed) :
                Dictates how fast the objects move
            affect_traffic(zombies, traffic, powers) :
                doesnt do anything in this class
            return_normal() :
                 returns speed and sprite of power up to normal
        -------
        """
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "invincible", 0.0005)

        self.power_up_type = "invincible"
        self.image = pygame.image.load(invincibility).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]

    # overriding abstract method
    def affect_player(self, player):
        """
        checks if player can collide
        if so, changes the sprite of the player to the "invincible" variant
        sets the "can_collide" attribute of the player to false
        saves the time
        teleports the invincible power up
        :param player: object of classs Car
        :return: None
        """
        if player.can_collide:
            player.image = pygame.image.load(invincibility_vehicles[player.vehicle_type]["invincible"]).convert_alpha()
            player.can_collide = False
            player.status_change_time = time.time()
            self.powerup_tp()

    def powerup_tp(self) -> None:
        """
        checks if the power up can spawn
        if so, teleports to the right of the screen
        if not, teleports to the left of the screen
        :return: None
        """
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def object_speed(self, speed):
        """
        Functions that dictates how fast
        the objects move to the left of the screen
        :param speed: int
        :return: None
        """
        self.rect.x -= self.speed * speed / 20

    def affect_traffic(self, zombies, traffic, powers):
        pass

    def return_normal(self):
        """
            Returns both the sprite and the speed to normal
            Used to return the power up back to normal after the slow power up
            :return: None
        """
        self.speed = 9
        self.image = pygame.image.load(invincibility).convert_alpha()

"""
Dictionary containing the information related the variant of the vehicles sprites
bear_trap: sprite of vehicle under the affect of bear_trap power up
invincible: sprite of vehicle under the affect of bear_trap power up
"""
invincibility_vehicles = {
    "car": {"bear_trap": stuck_car, "invincible": invincible_car},

    "bike": {"bear_trap": stuck_bike, "invincible": invincible_bike}
}


class BearTrap(PowerUp):
    """
        A class that represents the bear_trap power up
        ...
        Attributes
        probability : int
            probability of power up spawning, 0.0005
        position_x : int
            value of the x coordinate where the power up spawns
        position_y : int
            value of the y coordinate where the power up spawns
        speed : int
            speed at which the power up moves
        type : str
            "bear trap" used to attribute correct sprite for the slow visual effect
            using the slowed_sprites dictionary
        image : Surface
            sprite of the invincible power up
        rect : Rect
            creates a rectangle around the image
        rect.center : tuple
            sets the center of the rectangle at those coordinates
        hazard_mask : Mask
            creates a mask from the image
        damage : int
            damage the power up gives the player
        score : int
            score which the power up gives, after passing the left of the screen
        ----------
        Methods
            affect_player(player) :
                puts the player under the affect of the power up
            powerup_tp() :
                teleports power up
            object_speed(speed) :
                Dictates how fast the objects move
            affect_traffic(zombies, traffic, powers) :
                doesnt do anything in this class
            return_normal() :
                 returns speed and sprite of power up to normal
            get_damage() :
                 returns damage the power up gives
        -------
        """
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "beartrap", 0.002)

        self.power_up_type = "beartrap"
        self.image = pygame.image.load(bear_trap).convert_alpha()
        self.rect = self.image.get_rect()
        self.hazard_mask = pygame.mask.from_surface(self.image)
        self.rect.center = [position_x, position_y]
        self.damage = 3
        self.score = 25

    def affect_player(self, player):
        """
        checks if player can move
        if so, changes the sprite of the player to the "bear_trap" variant
        sets the "can_move" attribute of the player to false
        saves the time
        teleports the power up
        :param player: object of classs Car
        :return: None
        """
        if player.can_move:
            player.image = pygame.image.load(stuck_car).convert_alpha()
            player.can_move = False
            player.status_change_time = time.time()
            player.health -= self.get_damage()
            self.powerup_tp()

    def powerup_tp(self) -> None:
        """
        checks if the power up can spawn
        if so, teleports to the right of the screen
        if not, teleports to the left of the screen
        :return: None
        """
        if self.can_spawn():
            self.rect.center = [1400, random.choice([605, 682, 760])]
        else:
            self.rect.center = [-10, 0]

    def affect_traffic(self, zombies, traffic, powers):
        pass

    def return_normal(self):
        """
            Returns both the sprite and the speed to normal
            Used to return the power up back to normal after the slow power up
            :return: None
        """
        self.speed = 9
        self.image = pygame.image.load(bear_trap).convert_alpha()

    def get_damage(self):
        """
        gets the damage
        :return: damage
        """
        return self.damage

    def object_speed(self, speed):
        """
        Functions that dictates how fast
        the objects move to the left of the screen
        :param speed: int
        :return: None
        """
        self.rect.x -= self.speed * speed / 20


class SlowTime(PowerUp):
    """
    A class that represents the slowTime power up
        ...
        Attributes
        probability : int
            probability of power up spawning, 0.0005
        position_x : int
            value of the x coordinate where the power up spawns
        position_y : int
            value of the y coordinate where the power up spawns
        speed : int
            speed at which the power up moves
        type : str
            "slow_time" used to attribute correct sprite for the slow visual effect
            using the slowed_sprites dictionary
        image : Surface
            sprite of the invincible power up
        rect : Rect
            creates a rectangle around the image
        rect.center : tuple
            sets the center of the rectangle at those coordinates
        hazard_mask : Mask
            creates a mask from the image
        ----------
        Methods
            affect_player(player) :
                doesnt do anything in this class
            powerup_tp() :
                teleports power up
            object_speed(speed) :
                Dictates how fast the objects move
            affect_traffic(zombies, traffic, powers) :
                 puts everything besides the player under the affect of the power up
            return_normal() :
                 returns speed and sprite of power up to normal
        -------
        """
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, 9, "slow_time", 0.0002)
        self.power_up_type = "slow_time"
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
        """
        Functions that dictates how fast
        the objects move to the left of the screen
        :param speed: int
        :return: None
        """
        self.rect.x -= self.speed * speed / 20

    def affect_player(self, player):
        pass

    def return_normal(self):
        """
        Returns both the sprite and the speed to normal
        Used to return the power up back to normal after the slow power up
        :return: None
        """
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
