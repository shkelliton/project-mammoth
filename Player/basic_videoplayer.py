# Imbeds a video file within a Tkinter window
# tkVideo was made by Xenofon Konitsas - @huskeeeeee - konitsasx@gmail.com
# tkVideo can be found here https://github.com/huskeee/tkvideo
import tkinter as tk
from tkinter import *
from tkvideo import tkvideo
import pygame
import logging


root = tk.Tk()

pygame.mixer.init()

# currentAnimation = "Model\\polarbear_videoB0001-0080.mp4"
# backgroundMusic = "Sound\\coralbackgrnd.mp3"

def videoPlayBack(currentAnimation,backgroundMusic,varNarration):
    player = tkvideo(currentAnimation, my_label, loop = 1, size = (1920,1080))
    player.play()
    ##############################################
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load(backgroundMusic)
    pygame.mixer.music.play(loops=0)
    ##############################################
    global soundNarra
    soundNarra = pygame.mixer.Sound(varNarration)
    pygame.mixer.set_num_channels(1)
    soundNarra.set_volume(0.5)


def narration(root):
    pygame.mixer.Sound.play(soundNarra)


root.bind('c', narration)

polarBearButton = tk.Button(
    text="Click me for a Polar Bear!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=lambda: [videoPlayBack("Model\\polarbear_videoB0001-0080.mp4","Sound\\coralbackgrnd.mp3","Sound\\bear-growl.wav"), polarBearButton.pack_forget()]
)

polarBearButton.pack()
my_label = Label(root)
my_label.pack()

root.mainloop()
