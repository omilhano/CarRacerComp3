#TODO volume up and down
#TODO volume mute
import pygame

# Creating a function that creates the GUI
def setting():
    
    # initiating pygames
    pygame.init()
    custom_cursor = pygame.image.load('images/cursor.png').convert_alpha()
    #initialize at 720x720
    res = (974, 974)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Settings")
    # interface 
    while True:
        mouse = pygame.mouse.get_pos()
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #     if mouse[0] == 290 and mouse[1] == 530:
            #         print("Bullzeye") 
        # setting the background color as black
        bg = pygame.image.load("images/settings.jpg").convert_alpha()
        screen.blit(bg, (0,0))
        screen.blit( custom_cursor, mouse)

        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()