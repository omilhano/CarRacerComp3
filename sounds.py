from pygame import mixer
import pygame
volume = 0.6
first_time = True

def startingUp():
    global first_time
    if first_time:
        first_time = False
        global volume
        pygame.init()
        pygame.mixer.music.stop()
        mixer.music.unload()
        mixer.music.load("musicbackground.mp3")
        mixer.music.set_volume(volume)
        mixer.music.play()
        print("INSIDE OF STARTING UP", first_time)

def lower_volume():
    global volume
    volume -= 0.1
    pygame.mixer.music.set_volume(volume)
def increase_volume():
    global volume
    volume += 0.1
    pygame.mixer.music.set_volume(volume)
