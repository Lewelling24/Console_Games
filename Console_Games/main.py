#todo Implement game choice, and connect games with score keeping class

import os
from Guess_The_Num import Guess_The_Num as gn
from Tic_Tac_Toe import TicTacToe as TTT
from Rock_Paper_Scissors import rock_paper_scissors as rps


os.system('cls')

print("Welcome to console games! I've built out a few simple games you can play in the console.")
game_choice = int(input("Press 1 for Guess the Number, Press 2 for Rock Paper Scissors, Press 3 for Tic Tac Toe! "))

if(game_choice == 1):
    gn.Guess_The_Number_Computer()
elif(game_choice == 2):
    rps.rock_paper_scissors()
elif(game_choice == 3):
    TTT.tic_tac_toe()
else:
    print("That was not a valid choice.")



