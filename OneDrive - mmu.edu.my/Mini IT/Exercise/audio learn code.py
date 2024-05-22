import tkinter as tk
from tkinter import font
from random import shuffle
import pygame
import threading

# load BG music
pygame.mixer.music.load('background audio.mp3')
pygame.mixer.music.play(loops=-1, start=0.0) #repeat and where to start playing 
pygame.mixer.music.set_volume(.2) #volume



# Create the main application window
root = tk.Tk()


# Start playing background audio

# Start the Tkinter event loop
root.mainloop()
