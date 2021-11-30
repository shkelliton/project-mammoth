# Write your code here :-)
import tkinter as tk

window = tk.Tk()

# First Example
# label = tk.Label(text="Python rocks!")
# label.pack()

# Label Example
# label = tk.Label(
#     text="Hello, Tkinter",
#    #foreground="white", Set color to white
#    #background="black" Set the background color to black
#     fg="white",
#     bg="black",
#     width=10,
#     height=10
# )
# label.pack()

# Button Example
# button =tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
#button.pack()

# Entry Example
#def callback(window): #function gets entry box info and replaces label2 text
#    name = entry.get()
#    label2['text'] = name
#
#label = tk.Label(text="Name")
#label2 = tk.Label(text="")
#entry = tk.Entry(fg="yellow", bg="blue", width=50) #entry box
#label.pack() #pack order determines display order
#entry.pack()
#label2.pack()
#window.bind('<Return>', callback) #when the enter key is press call function

# Text Box
# text_box = tk.Text()
# text_box.pack()

# Frame Example
# frame_a = tk.Frame()
# frame_b = tk.Frame()
# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()
# frame_a.pack()
# frame_b.pack()


window.mainloop()