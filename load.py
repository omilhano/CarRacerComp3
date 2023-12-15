import pygame
import json
from car import Car
from garage import garage_screen
from healthbar import Healthbar


def continue_game():
    """
    Extracts value from the JSON file "load.json"
    Saves them as variables that will be used
    Directs player to the garage screen with the level completed
    :return: None
    """
    pygame.init()
    # Opening JSON file
    with open('load.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    playerCar = Car("car")
    # extracts the health value from JSON file
    playerCar.health = json_object["health"]
    # extracts the money value from the JSON file
    playerCar.money = json_object["money"]
    # extracts the score value from the JSON file
    playerCar.score = json_object["score"]
    healthbar = Healthbar(5, 5,100)
    healthbar.hp = playerCar.health
    garage_screen(playerCar, healthbar, json_object["level_completed"])
