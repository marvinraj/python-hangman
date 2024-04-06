def main():
    instructions()

    if play():
        print("works")
    else: 
        print("it does not work bro")

def play():
    user_choice = input("Are you ready to play? (y)es or (n)o\n")
    if user_choice == "n":
        return False
    elif user_choice == "y":
        return True

def get_words():
    random_words = ["apple", "terminator", "basketball"]



# function to display instructions
def instructions():
    print("\nH A N G  M A N")
    print("\nWelcome to Hangman! A word will be chosen at random and \nyou must try to guess the word correctly letter by letter \nbefore you run out of attempts. Good luck!\n")

if __name__ == "__main__":
    main()