import pygame
from config import cursor_img


class Cursor(pygame.sprite.Sprite):
    """
    A class that represents the cursor on the screen
    ...

    Attributes
    image : Surface
        sprite of the cursor
    rect : Rect
        creates a rectangle around the image
    ----------
    Methods
        update():
            updates the position of the cursor to the position of the mouse
    -------
    """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load(cursor_img).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        """
        Updates the position of the cursor to the position of the mouse
        :return: None
        """
        self.rect.center = pygame.mouse.get_pos()
