import random
import time

class Guess_The_Num:
    
    #Super simple guess the number game
    #Will return a W on win, and L on lose

    #Guess_The_Number_Player will be for the player to guess against the computer
    def Guess_The_Number_Player():

        computer_choice = random.randrange(0,11)

        guess_count = 0
        input_validation_flag = False

        while(guess_count < 3):

            while(not input_validation_flag):
                player_choice = int(input("Please choose a number between 0 and 10: "))
                if (player_choice >=0 and player_choice <= 10):
                    input_validation_flag = True
                else:
                    print("That is not a valid number for this game.")

            if(player_choice == computer_choice):
                print("You guessed the correct number, you win!")
                break
            else:
                print("You did not guess the correct number!")
                guess_count += 1
        if(guess_count < 3):
            return 'W'
        else:
            print("You did not guess the correct number in three tries, you lose!")
            return 'L'
                
        
    #This function will have the computer try and guess your number
    def Guess_The_Number_Computer():
       
        guess_count = 0
        input_validation_flag = False
       
        while(not input_validation_flag):
                player_choice = int(input("Please choose a number between 0 and 10: "))
                if (player_choice >=0 and player_choice <= 10):
                    input_validation_flag = True
                else:
                    print("That is not a valid number for this game.")

    
        while (guess_count < 3):
            computer_choice = random.randrange(0,11)
            time.sleep(2) # time delay for some realism

            if(computer_choice == player_choice):
                print("The computer was able to guess your number, you lose!")
                break
            else:
                print("The computer did not guess your number")
                guess_count += 1
        if(guess_count < 3):
            return 'L'
        else:
            print("The computer was unable to guess your number in three tries, you win!")
            return 'W'

