import random

BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}


def render():
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    # ----------------
    print(f"Turns taken: {game_round}", end="\n\n")
    print(f"{BOARD[1]} | {BOARD[2]} | {BOARD[3]}")
    print("- + - + -")
    print(f"{BOARD[4]} | {BOARD[5]} | {BOARD[6]}")
    print("- + - + -")
    print(f"{BOARD[7]} | {BOARD[8]} | {BOARD[9]}", end="\n\n")
    # ----------------


def get_action(player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    # ----------------
    global BOARD

    validPlays = ["X", "O"]

    #Player isn't a computer
    if player == "X":
        try: #player's turn
            play = int(input(f"Choose where you will play:"))

            while BOARD[play] in validPlays: #prevent replaying on the same space
                play = int(input(f"Spot taken, please try another."))

            #update the dictionary, count the turn.
            BOARD[play] = player

        except ValueError:
                print(f"'{play}' was not a valid entry.")
        except TypeError:
                print(f"'{play}' was not a valid entry.")
    
    #Player is the computer
    elif player == "O":
        try: #computer's turn
            play = random.randint(1,9)

            while BOARD[play] in validPlays: #prevent replaying on the same space
                play = random.randint(1,9)
                
            #update the dictionary
            BOARD[play] = player


        except ValueError:
            print(f"'{play}' was not a valid entry.")
               
    return play
        
    
    #if ' ' in BOARD.values():
    #    play = int(input(f"Choose where you will play from the following: "))
    #    BOARD[play] = player
    #    render()
    # ----------------

def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    # ----------------
    print(f"{player} won.", end="\n\n")
    
    # ----------------

def check_win(player, win):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''    
    # ----------------

    global BOARD

    if BOARD[1] == BOARD[2] == BOARD[3] == player:
        victory_message(player)
        win = True
        return win

    elif BOARD[4] == BOARD[5] == BOARD[6] == player:
        victory_message(player)
        win = True
        return win

    elif BOARD[7] == BOARD[8] == BOARD[9] == player:
        victory_message(player)
        win = True
        return win

    elif BOARD[1] == BOARD[5] == BOARD[9] == player:
        victory_message(player)
        win = True
        return win

    elif BOARD[3] == BOARD[4] == BOARD[7] == player:
        victory_message(player)
        win = True
        return win

    elif BOARD[1] == BOARD[4] == BOARD[7] == player:
        victory_message(player)
        win = True
        return win

    elif BOARD[2] == BOARD[5] == BOARD[8] == player:
        victory_message(player)
        win = True
        return win

    elif BOARD[3] == BOARD[6] == BOARD[9] == player:
        victory_message(player)
        win = True
        return win
    
    return win
    # ----------------

def play_t3():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''

    global BOARD
    global game_round  
    player = 'X'
    computer = 'O'
    spots_left = 9
    game_round = 0
    game_over = False
    win = False
    p1wins = 0
    p2wins = 0
    sysTies = 0
    choice = "y"

    current_player = "X"

    while choice == "y":

        # Print the current state of the board
        render()
        print(f"{spots_left} spaces available.")

        # Get the current player's action and assign it to a variable called 'action'.
        action = get_action(current_player)
        
        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.

        if game_round % 2 == 0:
            current_player = computer
        else:
            current_player = player

        # Increment the game round by 1.
        game_round += 1
        spots_left -= 1

        

        # Check if the game is winnable (game_round >= 4),
            # then check for win conditions (check_win(player)),
                # and if there's a win, end the game (game_over = True),
                # and break the loop (break).

        while spots_left <= 5 or spots_left != 0:
            if win == False:
                win = check_win(current_player, win)
                if win == True:
                    game_over = True
                    if current_player == "X":
                        p1wins += 1
                    elif current_player == "O":
                        p2wins += 1
                    print(f"Player score: {p1wins}. Computer score: {p2wins}. Scratches: {sysTies}.")
                else:
                    game_over = False
                break
            
            elif win == True:
                game_over == True
            
            elif spots_left == 0:
                render()
                print("It's a scratch. No winners.")
                sysTies += 1
                print(f"Player score: {p1wins}. Computer score: {p2wins}. Scratches: {sysTies}.")
                game_over == True
        
        if spots_left == 0 and game_over is False:
            render()
            print("It's a scratch. No winners.")
            sysTies += 1
            print(f"Player score: {p1wins}. Computer score: {p2wins}. Scratches: {sysTies}.")
        
        try:
            if win == True:
                game_over = True
                #break
        except:
            print("No winner yet.")

        # if spots_left <= 5:
        #     check_win(current_player)
        #     if win == True:
        #         game_over == True
        #         print(game_over, win)
        #         return game_over
        # elif spots_left == 0:
        #     render()
        #     print("It's a scratch. No winners.")
        #     game_over == True
        #     return game_over
        
        # Check if there are any open spots left (game_round == 9),
            # and if there aren't, print a tie message,
            # end the game,
            # and break the loop.

        # switch players with a quick conditional loop.
       

        if (' ' not in BOARD.values()) or game_over is True:
            render()
            choice = input("Play again? (y) to continue: ")
            if choice == "y":   
                #reset the board
                for key in BOARD:
                    BOARD[key] = " "
                #initializing the next round within the loop.
                game_over = False
                spots_left = 9
                game_round = 0
                win = False
            if choice != "y":
                game_over = True
                break
            
    # prompt for a restart and assign the input to a 'restart' variable.
    # if yes,
        # clear each key in the board with a for loop
        # and reinitiate the game loop (play_t3())


play_t3()
