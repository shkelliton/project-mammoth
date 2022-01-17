# Imbeds a video file within a Tkinter window
# tkVideo was made by Xenofon Konitsas - @huskeeeeee - konitsasx@gmail.com
# tkVideo can be found here https://github.com/huskeee/tkvideo
from tkinter import *
from tkvideo import tkvideo
import pygame

root = Tk()

pygame.mixer.init()

soundNarra = pygame.mixer.Sound("Sound\\coralbackgrnd.mp3")
soundNarra.set_volume(0.5)

def callback(root):
    player = tkvideo("Model\\polarbear_videoB0001-0080.mp4", my_label, loop = 1, size = (1920,1080))
    player.play()
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load("Sound\\coralbackgrnd.mp3")
    pygame.mixer.music.play(loops=0)

def narration(root):
    pygame.mixer.Sound.play(soundNarra)

root.bind('<Return>', callback)
root.bind('c', narration)

my_label = Label(root)
my_label.pack()

root.mainloop()
