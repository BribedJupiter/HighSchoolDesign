'''
Project:High School Design - CosmoGuessr
Libraries: tkinter
Authors: Jack Bauer, Jace Arnold, Zach Willingham, Sophia Jacob (Please fix your name if I got it wrong sorry lol - jack)
Date: 9/17/22
Last Modified: 9/17/22 by Jack
'''

# Imports our libraries
import tkinter as tk

# Define the other windows
def game():
    global game_window
    game_window = tk.Toplevel()
    game_window.title("CosmoGuessr")
    game_window.geometry("400x400")

# Creates the root window with a set title and a set height / width
root = tk.Tk()
root.title("Start")
root.geometry("400x400")

# Setup the start window
title_lbl = tk.Label(text="Welcome to CosmoGuessr", bg="black", fg="white", pady=10).pack() #bg = background color, fg = foreground color

begin_btn = tk.Button(text="Begin", bg="black",fg="gold", pady=10, command=game).pack() # command = function to call, pady = vertical space, .pack() tells it to put it on the screen

# Opens the window
root.mainloop()