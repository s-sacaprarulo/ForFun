import random
from typing import List
from typing import Dict
import tkinter as tk
from tkinter import messagebox
import threading
import os
import time
import pygame

__numberplayers__ = 4

def shot_fired(bullet_chambers:int, player_turn:int):
    number = random.randint(1, 6)

    if number <= bullet_chambers:
        # playing sound effects
        print("Lose")
        pygame.mixer.init()
        sound = pygame.mixer.Sound("C:/Users/1042113/Desktop/Cloned Repositories/ForFun/soundeffectLIB/Taco Bell Bong - Sound Effect (HD).mp3")
        sound.play()
        time.sleep(1.2)

        # getting the next player
        next_player = get_next_player_up(player_turn)
        out_players[player_turn] = False

        # checks if there is only one player left alive, if so, ends the game
        winning_player = any_more_players_alive()
        if  winning_player != None:
            messagebox.showinfo("Russian Roulette", f"player {winning_player} Wins!")
            return

        
        # continuing the game
        output = messagebox.askyesno("Russian Roulette", f"player {player_turn} dead! Player {next_player}'s turn!")
        if output:
            shot_fired(1, next_player)

    else:
        print("Win")
        pygame.mixer.init()
        sound = pygame.mixer.Sound("C:/Users/1042113/Desktop/Cloned Repositories/ForFun/soundeffectLIB/onlymp3.to - vine_boom-_vBVGjFdwk4-192k-1708393618.mp3")
        sound.play()

        time.sleep(1.2)
        next_player = get_next_player_up(player_turn)
        output = messagebox.askyesno("Russian Roulette", f"Player {next_player}'s turn!")
        if output:
            shot_fired(bullet_chambers + 1, next_player)


def get_next_player_up(current_player:int):


    next_up_player = current_player+1
    if next_up_player > __numberplayers__:
        next_up_player = 1
    while True:
        if out_players[next_up_player]:
            return next_up_player
        next_up_player += 1
        if next_up_player > __numberplayers__:
            next_up_player = 1

'''returns an int depending on who won. None if the game is not over'''
def any_more_players_alive() -> int:
    alive_players = 0
    live_player_index = None
    for i in range(len(out_players)):
        item = out_players.get(i)
        if item:
            alive_players += 1
            live_player_index = i
            if alive_players > 1:
                return None
    return live_player_index
            
            
    

# setting up the window
root = tk.Tk()
root.title("Russian Roulette")
root.geometry("400x300+100+100")
root.wm_attributes("-topmost", 1)

# creates starting variables
starting_player = random.randint(1, __numberplayers__)
out_players = dict()
for i in range(__numberplayers__):
    out_players[i + 1] = True

button = tk.Button(root, text=f"Player {starting_player} commences!", command=lambda: shot_fired(1, starting_player))
button.pack(pady=20)


root.mainloop()