import random

def hangman():
    """
    The classic Hangman game where players guess letters to uncover a hidden word.
    """
    # List of words to choose from
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php']
    
    # Choose a random word from the list
    word = random.choice(words)
    
    # Initialize variables
    guesses = ''
    turns = 6
    
    # Main game loop
    while turns > 0:
        # Counter for incorrect guesses
        failed = 0
        
        # Display the current state of the word
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1

        # Check if the word has been completely guessed
        if failed == 0:
            print('\nYou win!')
            break

        # Get the player's guess
        guess = input('\nGuess a letter: ')
        
        # Add the guess to the list of guesses
        guesses += guess

        # Check if the guess is incorrect
        if guess not in word:
            turns -= 1
            print('Incorrect')
            print(f'You have {turns} more guesses')

            if turns == 0:
                print('You lose!')
                print(f'The word was {word}')
    
    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        hangman()
    else:
        print("Thanks for playing!")

# Run the game
hangman()
