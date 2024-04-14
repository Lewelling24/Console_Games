#todo implement score keeping class for use with game classes

class Score_Keeper():
  
  #player_score, computer_score  = 0

  def __init__(self):
    self.player_score = 0
    self.computer_score = 0

  # constructor initializing player, and computer scores to a chosen number for counting down
  def __init__(self, starting_score):
    self.player_score = starting_score
    self.computer_score = starting_score
  
  # increment palyer, and computer score tallies
  def keep_count(character):
    if (character == 'W'):
      player_score += 1
    else:
      computer_score += 1

  # countdown scores
  def countdown_score(character)
    if(character == 'W'):
      computer_score -= 1
    else:
      player_score -= 1
  
  # based on computer, and player scores return C or P for winner, and T for tie
  def winner_determination():
    if( player_choice == computer_choice):
      return 'T'
    elif( player_score > computer_score):
      return 'P'
    else:
      return 'C'
