import random

def main():

    instructions()

    secret_word = get_word()
    chances = 10
    guessed_letters = []
    blank_word = []
    letters_to_guess = []

    play = True
    while play:
        print('\nGuess the following word! Please select a letter between A-Z.\n')

        # create blank version of the secret word
        for letter in secret_word:
            blank_word.append('_')
            letters_to_guess.append(letter)
        
        # print out the blank version of the secret word
        for i in blank_word:
            print(i, end=" ")
        
        # print an empty line so that the code looks better
        print("\n")

        # core game logic
        while chances != 0:
            guess = input("Guess a letter ==> ")
            if guess in letters_to_guess:
                print(f"{guess} is in the letters_to_guess")
            else:
                print("letter not found in word.")

        play = False

# a function to store a list of random words and returns a random word from the list
def get_word():
    random_words = ["apple", "orange", "lime"]
    chosen_word = random.choice(random_words)
    return chosen_word


# a function to display instructions
def instructions():
    print("\nH A N G  M A N")
    print("\nWelcome to Hangman! A word will be chosen at random and \nyou must try to guess the word correctly letter by letter \nbefore you run out of attempts. Good luck!\n")

if __name__ == "__main__":
    main()