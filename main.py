'''
Project:High School Design - CosmoGuessr
Libraries: tkinter
Authors: Jack Bauer, Jace Arnold, Zach Willingham, Sophia Jacob (Please fix your name if I got it wrong sorry lol - jack)
Date: 9/17/22
Last Modified: 9/17/22 by Jack
'''

'''
TODO: 
-Make it so enter key will go to next screen
-Make it so img is removed from list after it is used
-Make it so round, score, streak are updated after each round
'''

# Imports our libraries
import tkinter as tk # For the GUI
from PIL import ImageTk, Image # For displaying images - not sure if this is the best library to go with
import glob # For reading file paths, not sure if should go with this or not
import random # For random numbers 

# Setup our image library - not sure if this is the best spot to do this or if it matters
img = []
img_folder = 'Images'
for filename in glob.iglob(f"{img_folder}\*"):
    img.append(filename)
    print (filename)
print (img) # For debugging purposes - not sure why there are two backslashes in the names - "Images\\jupiter1.jpg"

# Setup game start values
total_rounds = 6 # Can make dynamic later, just putting this in for development right now
round = 1
score = 0
streak = 0

# Define the other windows, we will just call them as a function whenever we need to open the window. 
def game():
    # Setup the game window
    global game_window
    game_window = tk.Toplevel()
    game_window.title("CosmoGuessr")
    game_window.geometry("400x400")
    game_window.rowconfigure([0,1,2,3], minsize=100, weight=1) # Setup our grid
    game_window.columnconfigure([0,1,2], minsize=100, weight=1)

    # Setup the round number
    round_display = tk.Label(master=game_window, text=("Round: " + str(round) + "/" + str(total_rounds)))
    round_display.grid(row=0, column=0, sticky="nw")

    # Setup the score card
    score_display = tk.Label(master=game_window, text=("Score: " + str(score)))
    score_display.grid(row=0, column=1, sticky="n")

    # Setup the hot streak
    streak_display = tk.Label(master=game_window, text=("Hot Streak: " + str(streak)))
    streak_display.grid(row=0, column=3, sticky="ne")

    # Setup the Image
    global pic # Needs to be a global variable otherwise it won't display
    pic = ImageTk.PhotoImage(Image.open(random.choice(img)))
    img_display = tk.Label(game_window, image=pic)
    img_display.grid(row=1, column=1, sticky="nsew")

    # Setup the guessr entry form
    guess_lbl = tk.Label(master=game_window, text="Enter your guess:")
    guess_lbl.grid(row=2, column=0, sticky="se")
    guess_entry = tk.Entry(master=game_window, width=50)
    guess_entry.grid(row=2, column=1, sticky="s")

    # Setup next button
    next_btn = tk.Button(master=game_window, text="Next", command=game)
    next_btn.grid(row=2, column=2, sticky="se") 

    # game_window.bind("<Return>", game) # can't figure out why this doesn't work, but the actual button works so isn't too broken
        

def leaderboard():
    global leaderboard_window
    leaderboard_window = tk.Toplevel()
    leaderboard_window.title("Leaderboard")
    leaderboard_window.geometry("400x400")

# Creates the root window with a set title and a set height / width
root = tk.Tk()
root.title("Start")
root.geometry("400x400")

# Setup the start window
title_lbl = tk.Label(text="Welcome to CosmoGuessr", bg="black", fg="white", pady=10).pack() #bg = background color, fg = foreground color

begin_btn = tk.Button(text="Begin", bg="black",fg="gold", pady=10, command=game).pack() # command = function to call, pady = vertical space, .pack() tells it to put it on the screen

leaderboard_btn = tk.Button(text="Leaderboard",bg="black",fg="gold",pady=10, command=leaderboard).pack()

# Opens the window
root.mainloop()