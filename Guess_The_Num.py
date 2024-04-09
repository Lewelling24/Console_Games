import random

class Guess_The_Num:
    
    #Super simple guess the number game
    #Will return a W on win, and L on lose

    #Guess_The_Number_Player will be for the player to guess against the computer
    def Guess_The_Number_Player():

        computer_choice = random.randrange(0,101)

        player_choice = int(input("Please choose a number between 0 and 100 "))

        if(player_choice == computer_choice):
            print("You guessed the correct number, you win!")
            return 'W'
        else:
            print("You did not guess the correct number, you lose!")
            return 'L'
        
    #This function will have the computer try and guess your number
    def Guess_The_Number_Computer():
        player_choice = int(input("Please choose a number between 0 and 100 "))

        computer_choice = random.randrange(0,101)

        if(computer_choice == player_choice):
            print("The computer was able to guess your number, you lose!")
            return 'L'
        else:
            print("The computer did not guess your number, you win!")
            return 'W'

