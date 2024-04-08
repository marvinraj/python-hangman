import random

def main():

    instructions()

    secret_word = get_word()
    chances = 3
    guessed_letters = [] # not in secret word
    blank_word = []
    letters_to_guess = []

    play = True
    while play:
        print('\nGuess the following word! Please select a letter between A-Z.\n')

        # create blank version of the secret word
        for letter in secret_word:
            blank_word.append('_')
            letters_to_guess.append(letter)

        # core game logic
        while chances != 0:
            # print out the blank version of the secret word
            for i in blank_word:
                print(i, end=" ")
            
            # print guessed letters & chances left
            print(f"\n\nletters guessed but not in secret word: {guessed_letters}\nchances left : {chances}")

            guess = input("\n\nGuess a letter ==> ")

            print("=====================================================")

            if guess in letters_to_guess:
                print(f"\nNICEEEEE !! {guess} is in the word !!!!!!\n")
                letter_index = letters_to_guess.index(guess)
                blank_word[letter_index] = guess
                continue
            else:
                chances -= 1
                guessed_letters.append(guess)
                print("\nNOOOOBBBB letter not found in word.")

        print(f"\nYou ran out of chances. The secret word is {secret_word}")

        play = False

def show_blank():
    pass

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