import pygame

pygame.init()
# font
corbelfont = pygame.font.SysFont('Corbel', 40)  # Select font and size


#  draw healthbar
def draw(health_points, surface, vehicle):
    # calculate the ratio between current and max
    ratio = health_points.hp / health_points.max_hp
    pygame.draw.rect(surface, (217, 19, 68),
                     (health_points.x, health_points.y, health_points.width, health_points.height))
    pygame.draw.rect(surface, (88, 205, 132),
                     (health_points.x, health_points.y, health_points.width * ratio, health_points.height))
    if vehicle == "car":
        # display current car hp
        hp_car_text = corbelfont.render(f"HP: {int(health_points.hp)} (CAR)", True, (20, 46, 77))
        hp_car_rect = hp_car_text.get_rect(topleft=(10, 7))
        surface.blit(hp_car_text, hp_car_rect)
    else:
        # display current bike hp
        hp_bike_text = corbelfont.render(f"HP: {int(health_points.hp)} (BIKE)", True, (20, 46, 77))
        hp_bike_rect = hp_bike_text.get_rect(topleft=(810, 7))
        surface.blit(hp_bike_text, hp_bike_rect)


def display_score(score, surface):
    current_score = score
    score_surface = corbelfont.render(f" Score:{current_score}", False, (197, 136, 215))
    score_rect = score_surface.get_rect(center=(400, 30))
    surface.blit(score_surface, score_rect)


def display_money(money, surface):
    current_money = money
    money_surface = corbelfont.render(f" Money:{current_money}", False, (197, 136, 215))
    money_rect = money_surface.get_rect(center=(580, 30))
    surface.blit(money_surface, money_rect)


def display_time(surface):
    time_passed = int(pygame.time.get_ticks() / 1000)
    time_surface = corbelfont.render(f" Time:{time_passed}", False, (197, 136, 215))
    time_rect = time_surface.get_rect(center=(580, 30))
    surface.blit(time_surface, time_rect)
