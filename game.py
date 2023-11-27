import pygame, random
# Let's import the Car Class
from car_test import Car

# TODO avoid enemy collision on spawn
# solved by list with x position of the car, if x is the same then spawn them again

# TODO add health to car
# TODO add timer
# TODO add score

def car_racing():
    pygame.init()

    GREEN = (20, 255, 140)
    GREY = (210, 210 ,210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)

    bg = pygame.image.load("images/level1bg.jpg").convert()

    def pause():
        loop = True
        corbelfont = pygame.font.SysFont('Corbel', 50)  # Select font and size
        pausetext = corbelfont.render("Game is Paused", True, (100, 25, 225))
        spacebartext = corbelfont.render("Press Spacebar to continue", True, (100,25,225)) 
        screen.blit(pausetext, [200,200]) 
        screen.blit(spacebartext,[200,250]) 
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        screen.fill((0, 0, 0))
                        loop = False
            pygame.display.update()
            clock.tick(60)
    speed = 1

    

    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)


    SCREENWIDTH=1282
    SCREENHEIGHT=800

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()


    playerCar = Car(RED, 250, 250, 70)
    playerCar.car_rect.x = 200
    playerCar.car_rect.y = SCREENHEIGHT - 200

    # car1 = Car(PURPLE, 60, 80, random.randint(50,100))
    # car1.rect.x = 1000
    # car1.rect.y = SCREENHEIGHT - 250
    #
    # car2 = Car(YELLOW, 60, 80, random.randint(50,100))
    # car2.rect.x = 1300
    # car2.rect.y = SCREENHEIGHT - 200
    #
    # car3 = Car(CYAN, 60, 80, random.randint(50,100))
    # car3.rect.x = 1400
    # car3.rect.y = SCREENHEIGHT - 100
    #
    # car4 = Car(BLUE, 60, 80, random.randint(50,100))
    # car4.rect.x = 1500
    # car4.rect.y = SCREENHEIGHT - 100


    # Add the car to the list of objects
    all_sprites_list.add(playerCar)
    # all_sprites_list.add(car1)
    # all_sprites_list.add(car2)
    # all_sprites_list.add(car3)
    # all_sprites_list.add(car4)


    all_coming_cars = pygame.sprite.Group()
    # all_coming_cars.add(car1)
    # all_coming_cars.add(car2)
    # all_coming_cars.add(car3)
    # all_coming_cars.add(car4)


    #Allowing the user to close the window...
    carryOn = True
    clock=pygame.time.Clock()
    
    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         playerCar.moveRight(10)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                playerCar.moveLeft(5)
            if keys[pygame.K_d]:
                playerCar.moveRight(5)
            if keys[pygame.K_w]:
                playerCar.moveBackward(5)
            if keys[pygame.K_s]:
                playerCar.moveForward(5)
            if keys[pygame.K_p]:
                playerCar.repaint(GREEN)
            if keys[pygame.K_ESCAPE]:
                pause()
            
            #Game Logic
            for car in all_coming_cars:
                car.objectSpeed(speed)
                if car.rect.right < 0:  
                    car.changeSpeed(random.randint(100,200))
                    car.repaint(random.choice(colorList))
                    car.rect.x = SCREENWIDTH + car.width  
                    car.rect.y = random.randint(600, 700)  

                    collision = False
                    for existing_car in all_coming_cars:
                        if existing_car.rect.colliderect(pygame.Rect(car.rect.x, car.rect.y, car.width, car.height)):
                            collision = True
                            break
        
                    if not collision:
                        car.changeSpeed(random.randint(100,200))
                        car.repaint(random.choice(colorList))
                        car.rect.x = SCREENWIDTH + 3* car.width
                        car.rect.y = random.randint(600, 700)

                # Check if there is a car collision (player enemy)
                car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
                for car in car_collision_list:
                    print("Car crash!")
                    # End Of Game
                    carryOn = True

            all_sprites_list.update()
            
            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)

            screen.blit(bg, (0,0))
            screen.blit(playerCar.showmask, (0,0))
            # all_sprites_list.draw(screen)

 
            #Refresh Screen
            pygame.display.flip()

            #Number of frames per secong e.g. 60
            clock.tick(60)

    pygame.quit()