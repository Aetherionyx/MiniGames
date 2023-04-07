''' This is the main file. Run this file to select and play a particular
    game.'''


game_lib = {
    1: "Tic-Tac-Toe",
    2: "Rock Paper Scissors",
    3: "Checkers"
}

while True:
    print("""
Your game library:
1: Tic-Tac-Toe
2: Rock Paper Scissors
3: Checkers
exit: quit menu
""")
    game_choice = input("""
What game would you like to play?
Input the game ID, or type 'exit' to exit.
""")

    if game_choice == '1':
        try:
            from pyGames.tictactoe.py import *
            play_t3()
            game_choice = None
        except:
            print("Game not found.")

    elif game_choice == '2':
        try:
            from pyGames.rockPaperScissors.py import * 
            play_rps()
            game_choice = None
        except:
            print("Game not found.")

    elif game_choice == '3':
        try:
            from pyGames.numberGame.py import * 
            play_numGuesser()
        except:
            print("Game not found.")

    elif game_choice == 'exit':
        break