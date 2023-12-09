import pygame

pygame.init()
#     font
corbelfont = pygame.font.SysFont('Corbel', 40)  # Select font and size


#  draw healthbar
def draw(health_points, surface):
    # calculate the ratio between current and max
    ratio = health_points.hp / health_points.max_hp
    pygame.draw.rect(surface, (217, 19, 68),
                     (health_points.x, health_points.y, health_points.width, health_points.height))
    pygame.draw.rect(surface, (88, 205, 132),
                     (health_points.x, health_points.y, health_points.width * ratio, health_points.height))
    # display current hp
    hp_text = corbelfont.render(f"HP: {int(health_points.hp)}", True, (20, 46, 77))
    hp_rect = hp_text.get_rect(topleft=(10, 7))
    surface.blit(hp_text, hp_rect)


def display_score(score, surface):  # TODO utils
    current_score = score
    score_surface = corbelfont.render(f" Score:{current_score}", False, (197, 136, 215))
    score_rect = score_surface.get_rect(center=(400, 30))
    surface.blit(score_surface, score_rect)


def display_money(money, surface):  # TODO utils
    current_money = money
    money_surface = corbelfont.render(f" Money:{current_money}", False, (197, 136, 215))
    money_rect = money_surface.get_rect(center=(580, 30))
    surface.blit(money_surface, money_rect)
