import random
import time
class rock_paper_scissors:
    #prints win/lose/tie to the console, returns character for outcome
    #returns P for player win, C for computer win, T for tie

    def __init__(self):
        pass
    
    def rock_paper_scissors():
        computer_player_choice = random.randrange(0, 3)
        
        player_choice = input("Please choose Rock, Paper or Scissors: ")

        time.sleep(1)
        
        if(computer_player_choice == 0):
            print("The Computer chose Rock.")
        elif(computer_player_choice == 1):
            print("The Computer chose Paper.")
        else:
            print("The Computer chose Scissors.")

        time.sleep(1)

        print("You chose " + player_choice + ".")
        match player_choice:
            case "Rock":
                player_choice = 0
            case "Paper":
                player_choice = 1
            case "Scissors":
                player_choice = 2

        
        time.sleep(1)

        if(player_choice == computer_player_choice): #Tie first to save time
            print("It's a tie!")
            return 'T'
        elif player_choice == 2:
            if(computer_player_choice == 0):
                print("You lose!")
                return 'C'
            else:
                print('You win!')
                return 'P' 
        elif computer_player_choice == 2:
            if(player_choice == 0):
                print("You win!")
                return 'P'
            else:
                print('You lose!')
                return 'C'
        elif computer_player_choice > player_choice:
            print("You lose")
            return 'C'
        else:
            print("You win!")
            return 'P'
