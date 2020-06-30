def guessing_game():
    secretWord = "blue"
    guessesRemaining = 5
    gameWon = False
    while guessesRemaining > 0:
        currentGuess = input("What do you think the secret word is?\t")
        if (currentGuess.lower() == secretWord):
            print("You got it right!")
            gameWon = True
            break
        else:
            guessesRemaining -= 1
            if (guessesRemaining > 0):
                print("That's not right! You have " + str(guessesRemaining) + (" guesses" if guessesRemaining > 1 else " guess") +  " remaining.")

    if (gameWon):
        print("You won, congrats!")
    else:
        print("Better luck next time!")

guessing_game()