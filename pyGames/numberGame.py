#get a randomly generated number and guess it!
import random

def check_win(number, guess):
    if guess < number:
        verdict = "Guess higher."
    elif guess > number:
        verdict = "Guess lower."
    elif guess == number:
        verdict = "Nailed it!"

    return verdict

def play_numGuesser():
    totalWins = 0
    remainingGuesses = 5
    number = random.randint(1,30)

    guess = int(input("Guess a number in the range of 1-30: "))
    verdict = check_win(number, guess)
    print(verdict)

    if verdict == "Nailed it!":
            totalWins += 1
            print(f"Your score: {totalWins}")

    while number != guess or remainingGuesses != 0:
        
        if verdict == "Guess higher.":
            guess = int(input("Pick a higher number in the range of 1-30: "))
        elif verdict == "Guess lower.":
            guess = int(input("Pick a lower number in the range of 1-30: "))

        verdict = check_win(number, guess)
        print(verdict)

        if verdict == "Nailed it!":
            totalWins += 1
            print(f"Your score: {totalWins}")

        remainingGuesses -= 1

    decision = input("Continue? (y) to continue.")
    if decision == "y":
        play_numGuesser()
    
play_numGuesser()