# Main.py
# By: Arely Aguirre, Tristan Dewing

from hangman import Hangman
from drawing import drawing

def play_hangman():
    ''' 
      Plays hangman game
      Arguments:
        None
      Returns:
        None, but prints out dialogue of game
    '''
    word_file = open("words.txt", "r")
    game = Hangman(word_file)

    print("Welcome to Hangman!\n")
    drawing(game.life_counter)
    print("The mystery word has {} letters\n".format(len(game.mystery_word)))
    while game.life_counter != 0 and game.guessed_word != game.mystery_word_list:
        # Check for already guessed letters and non-letters
        print(" ".join(game.guessed_word)+"\n")
        game.guess = input("Guess a letter or guess a word.\nYour letter options are {}:\n"
                      .format(" ".join(game.letter_bank))).lower().strip()
        try:
            assert game.guess.isalpha()
        except AssertionError:
            print("\nCharacter must be a letter. Please choose a letter.\n")
            continue
        else:
            try:
                assert game.guess not in game.guessed_letters
            except AssertionError:
                print("\nYou already guessed this letter. Please choose another letter.\n")
                continue

        # Check if valid guess is in word
        if len(game.guess) == 1:
            # only appends letters
            game.guess_letters()
        try:
            game.remove_guess()
            # this will only work is guess is a single letter
        except ValueError:
            print("\nAre you sure you want to guess this word? If incorrect you will lose ALL your lives!")
            cont = input("Type \"yes\" if you want to continue with this word. Otherwise type \"no\": ").lower().strip()
            if cont == "yes":
                if game.guess == game.mystery_word:
                    game.guessed_word = list(game.guess)
                    print("\n")
                else:
                    game.life_deductor(game.life_counter)
                    drawing(game.life_counter)
            else:
                print("\n")
            continue

        # Instance of exception handling
        if game.guess in game.mystery_word_list:
            indices = [i for i, letter in enumerate(game.mystery_word_list) if letter == game.guess]
            for i in indices:
                game.guessed_word[i] = game.guess
            print("\nSuccessful guess!")
            drawing(game.life_counter)   
        else:
            game.life_deductor(1)
            print("\nSorry wrong guess!")
            drawing(game.life_counter)
            if game.life_counter == 1:
                print("You have 1 life left.\n")
            else:
                print("You have {} lives left.\n".format(game.life_counter))

    # Determine if player won or lost
    if game.life_counter == 0:
        print("You lost!\nThe correct word was '{}'".format(game.mystery_word))
    else:
        print("You win!\nYou guessed the word '{}' correctly!".format(game.mystery_word))
        
if __name__ == "__main__":
    play_hangman()