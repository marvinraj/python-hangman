import random

def main():

    instructions()
    start_game()
    

def start_game():
    print("Are you ready to play?")
    user_play = input("==> ")

    if user_play == "y":
        core_game()
    elif user_play == "n":
        print("ok bye")
        exit()

# core game logic
def core_game():
    secret_word = get_word()
    chances = 3
    guessed_letters = [] # not in secret word
    blank_word = []
    letters_to_guess = []

    play = True
    while play:
        print('\nGuess the following word! Please select a letter between A-Z.\n')

        # create blank version of the secret word
        create_blank_word(blank_word, secret_word, letters_to_guess)

        # core game logic
        while chances != 0:
            # print out the blank version of the secret word
            print_blank_word(blank_word)

            # check guessed word
            if ''.join(blank_word) == secret_word:
                print(f'\n\nYOU GUESSED IT RIGHT!! The secret word is {secret_word}.')
                break

            # print guessed letters & chances left
            print(f"\n\nletters guessed but not in secret word: {guessed_letters}\nchances left : {chances}")

            # user guesses a letter
            guess = input("\n\nGuess a letter ==> ")

            print("\n=======================================================================")

            # checks if guessed letter is in the secret word
            if guess in letters_to_guess: # letter in word
                print(f"\nNICEEEEE !! {guess} is in the word !!!!!!\n")
                letter_index = letters_to_guess.index(guess)
                blank_word[letter_index] = guess
                continue
            else: # letter not in word
                chances -= 1
                guessed_letters.append(guess)
                print("\nNOOOOBBBB letter not found in word.")
        
        play = False
    
    print(f"\nYou ran out of chances. The secret word is {secret_word}")


# a function to create blank version of the secret word        
def create_blank_word(blank_word, secret_word, letters_to_guess):
    for letter in secret_word:
        blank_word.append('_')
        letters_to_guess.append(letter)

# a function to print out the blank version of the secret word
def print_blank_word(blank_word):
    for i in blank_word:
        print(i, end=" ")
    
# a function to store a list of random words and returns a random word from the list
def get_word():
    random_words = ["pen", "orange", "lime"]
    chosen_word = random.choice(random_words)
    return chosen_word

# a function to display instructions
def instructions():
    print("\nH A N G  M A N")
    print("\nWelcome to Hangman! A word will be chosen at random and \nyou must try to guess the word correctly letter by letter \nbefore you run out of attempts. Good luck!\n")

if __name__ == "__main__":
    main()