# Imbeds a video file within a Tkinter window
from tkinter import *
from tkvideo import tkvideo

root = Tk()
my_label = Label(root)
my_label.pack()
player = tkvideo("C:\\Users\\Matthew\\Videos\\polarbear_videoB0001-0080.mp4", my_label, loop = 1, size = (1280,720))
player.play()

root.mainloop()
