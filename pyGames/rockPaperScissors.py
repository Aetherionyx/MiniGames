import random

#rock paper scissors dictionary
validMoves = ("r", "p", "s")
continueOptions = ("y", "n")
#INITIALIZATION
player1, player2 = "Player", "Computer"
decision, counter, p1wins, p2wins, ties = "y", 0, 0, 0, 0


def decide_winner(play1, play2):
  
  global validMoves

  #determine winners
  if play1 == "r" and play2 == "p":
    winner = "Computer"
  elif play1 == "p" and play2 == "r":
    winner = "Player"
  elif play1 == "s" and play2 == "r":
    winner = "Computer"
  elif play1 == "r" and play2 == "s":
    winner = "Player"
  elif play1 == "s" and play2 == "p":
     winner = "Player"
  elif play1 == "p" and play2 == "s":
    winner = "Computer"
  elif (play1 == play2) and (play1 in validMoves) and (play2 in validMoves):
    print(f"It's a tie between {player1} and {player2}.")
    winner = "No one"
  else:
    print("Invalid Selections Detected.")
    #game didn't play
    winner = "No one"
    
  return(winner)

def play_rps():
  
  decision = "y"
  counter = 0
  p1wins = 0
  p2wins = 0
  mutualTies = 0

  #game loop
  while decision == "y" and (p1wins < 3 or p2wins < 3):
    #make a choice on what to play
    play1, play2 = input(f"{player1}'s turn. Make your play by choosing rock (r), paper (p), or scissors (s)!: "), random.choice(validMoves)
    #count the game total
    counter += 1

    #wins
    winner = decide_winner(play1, play2)
    if winner == "Player":
      p1wins += 1
    elif winner == "Computer":
      p2wins += 1
    elif winner == "No one":
      mutualTies += 1

    print(f"{winner} won! Player has a score of {p1wins}, computer has a score of {p2wins}, and the tie board is at {mutualTies} total.")
    print(f"{counter} game(s) played.", end="\n\n")
    
    #overrides
    if p1wins == 3 or p2wins == 3:
      print("Maximum plays reached.")
      decision = "n"
    elif decision == "y":
      decision = input("Play again? Yes (y) or no (n): ")
      while decision not in continueOptions:
        decision = input("Error, invalid input: Play again? Yes (y) or no (n): ")

play_rps()
    