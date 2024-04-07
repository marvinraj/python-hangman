import random

def main():
    instructions()
    play = True
    secret_word = get_words()
    chances = 10
    guessed_letters = []
    word_to_guess = []

    while play:
        print('\nGuess the following word! Please select a letter between A-Z.\n')

        # create blank version of the secret word
        for letter in secret_word:
            word_to_guess.append('_')
        
        # print out the blank version of the secret word
        for i in word_to_guess:
            print(i, end=" ")
        
        # print an empty line so that the code looks better
        print("\n")

        play = False

# a function to store a list of random words and returns a random word from the list
def get_words():
    random_words = ["apple", "orange", "lime"]
    chosen_word = random.choice(random_words)
    return chosen_word


# a function to display instructions
def instructions():
    print("\nH A N G  M A N")
    print("\nWelcome to Hangman! A word will be chosen at random and \nyou must try to guess the word correctly letter by letter \nbefore you run out of attempts. Good luck!\n")

# def play():
#     user_choice = input("Are you ready to play? (y)es or (n)o\n")
#     if user_choice == "n":
#         return False
#     elif user_choice == "y":
#         return True

if __name__ == "__main__":
    main()