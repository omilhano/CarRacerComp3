import pygame
from pygame import mixer


volume = 0.6
first_time = True
music_paused = False

def startingUp():
    """
    Function controls the music playing on
    :return: None
    """
    global first_time
    if first_time:
        first_time = False
        global volume
        pygame.init()
        pygame.mixer.music.stop()
        mixer.music.unload()
        mixer.music.load("sounds/musicbackground.mp3")
        mixer.music.set_volume(volume)
        mixer.music.play()


def lower_volume():
    global volume
    volume -= 0.1
    pygame.mixer.music.set_volume(volume)


def increase_volume():
    global volume
    volume += 0.1
    pygame.mixer.music.set_volume(volume)


# mute and unmute
def pause():
    global music_paused
    if music_paused:
        mixer.music.play()
        music_paused = False
    else:
        mixer.music.pause()
        music_paused = True
