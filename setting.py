#TODO volume up and down
#TODO volume mute
import pygame

# Creating a function that creates the GUI
def setting():
    black = (0,0,0)
    # initiating pygames
    pygame.init()
    #initialize at 720x720
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("Settings")
    # interface 
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
        # setting the background color as black
        screen.fill(black)
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()