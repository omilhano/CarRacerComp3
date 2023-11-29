import pygame

def credits_():
    TEXTCOLOR = (255,101,80)
    pygame.init()
    custom_cursor = pygame.image.load('images/cursor.png').convert_alpha() # TODO change to sprite cursor
    res = (1282, 800)
    screen = pygame.display.set_mode(res)
    arialfont = pygame.font.SysFont('arial', 50)
    credit_text_alex = arialfont.render('Alexandre Francisco 20221512', True, TEXTCOLOR)
    credit_text_eli = arialfont.render('Eli Godinho, 20221781', True, TEXTCOLOR)
    while True:
        mouse = pygame.mouse.get_pos()
        #solves circular import
        from mainmenu import menu
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on menu button to go back
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if 995 <= mouse[0] <= 1230 and 630<= mouse[1] <= 775:    
                  menu()  
            
        bg = pygame.image.load("images/credits.png").convert_alpha()
        screen.blit(bg,(0,0))
        screen.blit(credit_text_alex, (0,0))
        screen.blit(credit_text_eli,(0,50))
        screen.blit( custom_cursor, mouse)
        pygame.display.update()