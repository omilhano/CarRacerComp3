import pygame
import json
import os
from config import continue_scr
from car import Car
from garage import garage_screen
from healthbar import Healthbar


def continue_game():
    pygame.init()

    # Opening JSON file
    with open('load.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    playerCar = Car(130, 680, 70)
    playerCar.health = json_object["health"]
    playerCar.money = json_object["money"]
    playerCar.score = json_object["score"]
    healthbar = Healthbar(5, 5, 300, 40, 100)
    healthbar.hp = playerCar.health
    garage_screen(playerCar, healthbar, json_object["level_completed"])
