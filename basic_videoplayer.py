# Imbeds a video file within a Tkinter window
# tkVideo was made by Xenofon Konitsas - @huskeeeeee - konitsasx@gmail.com
# tkVideo can be found here https://github.com/huskeee/tkvideo
from tkinter import *
from tkvideo import tkvideo
import pygame

root = Tk()

pygame.mixer.init()

def callback(root):
    player = tkvideo("C:\\Users\\Matthew\\Documents\\Github\\project-mammoth\\Model\\polarbear_videoB0001-0080.mp4", my_label, loop = 0, size = (1920,1080))
    player.play()
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load("C:\\Users\\Matthew\\Documents\\Github\\project-mammoth\\Sound\\coralbackgrnd.mp3")
    pygame.mixer.music.play(loops=0)


root.bind('<Return>', callback)

my_label = Label(root)
my_label.pack()

root.mainloop()
