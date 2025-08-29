import random

def information_game():
    
    print("""

        Bagels, a deductive logic game.
        By Al Sweigart al@inventwithpython.com
        I am thinking of a 3-digit number. Try to guess what it is.

          """)
    


def game_rules():
    
    print("""

        Here are some clues:
        I say:    That means:
        Pico         One digit is correct but in the wrong position.
        Fermi        One digit is correct and in the right position.
        Bagels       No digit is correct.

        """)
    
def get_user_guess():
    while True:
        guess = input("> ")
        if len(guess) == 3 and guess.isdigit():
            return list(guess)
        else:
            print("Chyba: zadej prosím 3 ciferné číslo.")



def main():

    # guessed number; guess count; list fo hits
    GUSSED_NUM = list(str(random.randint(100,999)))
    guess_count = 10
    hint = []

    
    # information about creator:
    information_game()


    # setting game rules:
    game_rules()

    while guess_count > 0:

        # reuse hint
        hint.clear()

        # user guess, guess count 
        print(f"Guess #{guess_count}")
        user_guess = get_user_guess()
        

        # Equal to guess number

        if user_guess == GUSSED_NUM:
            print("You got it!")
            print("Wanted number: ")
            print(int("".join(GUSSED_NUM)))
            break

        
        # Check for hints

        for index, value in enumerate(user_guess):

            if GUSSED_NUM[index] == value:
                hint.append("Fermi")
            elif value in GUSSED_NUM:
                hint.append("Pico")

        if len(hint) == 0:
            print("Bagels")


        print(" ".join(hint))

        guess_count -= 1

    print("You tried. Wanted number was: ")
    print(int("".join(GUSSED_NUM)))



if __name__ == "__main__":
    main()
