import pygame

from car import Car
from cursor import Cursor


# TODO image background
# TODO define powerups
# TODO give car money attribute
# TODO give car health upgrade attribute
# TODO give car damage (??) attribute
def garage_screen(playerCar):
    pygame.init()

    # looks dumb ask Liah
    playerCar = playerCar

    # defining screen/background
    bg = pygame.image.load("images/garage.png").convert_alpha()
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Car Racing")
    custom_cursor = Cursor()
    cursor_group = pygame.sprite.Group()
    cursor_group.add(custom_cursor)
    cursor_group.add(custom_cursor)
    clock = pygame.time.Clock()

    def upgrade_health():
        playerCar.max_hp += 10

    def recover_health():
        playerCar.health += 10

    upgrade_health()
    print(playerCar.health)
    while True:
        mouse = pygame.mouse.get_pos()
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 475 <= mouse[0] <= 735 and 595 <= mouse[1] <= 712:
                    pygame.quit()
            # press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 785 <= mouse[0] <= 1130 and 440 <= mouse[1] <= 595:
                    pass
            # pressing the play button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= mouse[0] <= 445 and 140 <= mouse[1] <= 295:
                    pass
            # pressing the continue game button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 787 <= mouse[0] <= 1130 and 138 <= mouse[1] <= 292:
                    pass
                    # pressing the settings button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 98 <= mouse[0] <= 445 and 443 <= mouse[1] <= 598:
                    pass

            # test position of the mouse
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())

        # setting background
        screen.blit(bg, (0, 0))
        # draw mouse
        cursor_group.draw(screen)
        cursor_group.update()

        # PYGAME BUILT-IN FUNCTION that updates the screen at every iteration of the loop
        pygame.display.flip()

        # frames
        clock.tick(60)
