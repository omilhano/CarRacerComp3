import sys
import pygame
from pygame import mixer
from cursor import Cursor
from mainmenu import menu
from config import icon_image, title_menu, main_sound

# starting music
mixer.init()
mixer.music.load(main_sound)
mixer.music.set_volume(0.7)
mixer.music.play()


# Creating a function that creates the GUI
def interface():
    pygame.init()
    # making cursor invisible
    pygame.mouse.set_visible(False)
    # setting game icon
    icon = pygame.image.load(icon_image)
    pygame.display.set_icon(icon)
    # initialize at certain res
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    pygame.display.set_caption("Driven to Decay : Byte the Dust")
    # interface loop
    while True:
        pygame.mouse.get_pos()
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                sys.exit()
            elif ev.type == pygame.KEYDOWN:
                # Check if ENTER/Return is KEYDOWN
                if ev.key == pygame.K_RETURN:
                    mixer.music.load("sounds/enginerev.mp3")
                    mixer.music.set_volume(0.7)
                    mixer.music.play()
                    pygame.time.delay(1000)
                    menu()
        # setting the background as image
        bg = pygame.image.load(title_menu)
        # startmenu = pygame.image.load("pressthis.png").convert_alpha()
        # INSIDE OF THE GAME LOOP
        screen.blit(bg, (0, 0))
        cursor_group.draw(screen)
        cursor_group.update()
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()
