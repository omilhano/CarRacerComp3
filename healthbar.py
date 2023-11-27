import pygame


class Healthbar():

    def __init__(self, x, y, width, height, max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        # font
        corbelfont = pygame.font.SysFont('Corbel', 40)  # Select font and size
        # calculate the ratio between current and max
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, (217,19,68), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, (88,205,132), (self.x, self.y, self.width * ratio, self.height))
        # display current hp
        hp_text = corbelfont.render(f"HP: {int(self.hp)}", True, (20, 46, 77))
        hp_rect = hp_text.get_rect(topleft=(10, 7))
        surface.blit(hp_text, hp_rect)
