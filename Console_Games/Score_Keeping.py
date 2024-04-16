#todo implement score keeping class for use with game classes

class Score_Keeper():
  
  player_score = 0 
  computer_score = 0

  def __init__(self):
    self.player_score = 0
    self.computer_score = 0

    # based on computer, and player scores return C or P for winner, and T for tie
  def return_winner(self):
    if(self.player_score == self.computer_score):
      return 'T'
    elif (self.player_score > self.computer_score):
      return 'P'
    else:
      return 'C'

  # constructor initializing player, and computer scores to a chosen number for counting down
  def __init__(self, starting_score):
    self.player_score = starting_score
    self.computer_score = starting_score
  
  # increment palyer, and computer score tallies
  def keep_count(self,character):
    if (character == 'W'):
      self.player_score += 1
    elif(character == 'C'):
      self.computer_score += 1
    else:
      print('Neither player wins, scores not updated')

  # countdown scores
  def countdown_score(self,character):
    if(character == 'W'):
      self.computer_score -= 1
    else:
      self.player_score -= 1
  
  

