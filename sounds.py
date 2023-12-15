import pygame
from pygame import mixer


volume = 0.6

"""
    first_time is a global bool variable used to prevent the music from restarting
    when changing screens
"""
first_time = True

music_paused = False

def startingUp():
    """
    Function controls the music playing on the background
    while in-game

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
    """
    Function that is activated when pressing the "lower" button
    on the settings.py file by passing a new value to pygame.mixer

    :return: None
    """
    global volume
    volume -= 0.1
    pygame.mixer.music.set_volume(volume)


def increase_volume():
    """
    Function that is activated when pressing the "higher" button
    on the settings.py file by passing a new value to pygame.mixer

    :return: None
    """
    global volume
    volume += 0.1
    pygame.mixer.music.set_volume(volume)


# mute and unmute
def pause():
    """
    Checks if music is paused
    If true, then resumes the musics
    If false, then pauses the music

    :return:
    """
    global music_paused
    if music_paused:
        mixer.music.play()
        music_paused = False
    else:
        mixer.music.pause()
        music_paused = True
