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
