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
    #starts the game using a txt file of words as input

    print("Welcome to Hangman!\n")
    drawing(game.life_counter)
    print("The mystery word has {} letters\n".format(len(game.mystery_word)))
    
    while game.life_counter != 0 and game.guessed_word != game.mystery_word_list:
        #game continues as long as player has lives and hasn't guessed the correct wod
     
        print(" ".join(game.guessed_word)+"\n")
        #displays dashes and letters
        #updates as the player makes succesful guesses
        
        game.guess = input("Guess a letter or guess a word.\nYour letter options are {}:\n"
                      .format(" ".join(game.letter_bank))).lower().strip()
        #prompts user to make a guess and displays possible letter options
        
        try:
        #instance of exception handling
            assert game.guess.isalpha()
            #makes sure input is a letter or string of letters
        except AssertionError:
            print("\nCharacter must be a letter. Please choose a letter.\n")
            continue
            #game returns to beginning of while loop, allows user to make a new valid guess
        else:
            try:
                assert game.guess not in game.guessed_letters
                #makes sure input has not already been guessed
            except AssertionError:
                print("\nYou already guessed this letter. Please choose another letter.\n")
                continue
                #game returns to beginning while loop, allows user to make a new guess

       
        if len(game.guess) == 1:
            game.guess_letters()
            #only appends letters
            #words are not added to guessed letters list
        try:
        #instance of exception handling
            game.remove_guess()
            # guess will only be removed from letter_bank if
            # it is a singular letter, an error will be raised otherwise
        except ValueError:
            print("\nAre you sure you want to guess this word? If incorrect you will lose ALL your lives!")
            cont = input("Type \"yes\" if you want to continue with this word. Otherwise type \"no\": ").lower().strip()
            #confirms with user that they want to guess this word
            if cont == "yes":
                if game.guess == game.mystery_word:
                    game.guessed_word = list(game.guess)
                    print("\n")
                    #user succesfully guessed the mystery word
                else:
                    game.life_deductor(game.life_counter)
                    drawing(game.life_counter)
                    #user incorrectly guessed mystery word and lost remaining lives
            else:
                print("\n")
            continue
            #code returns to beginning of while loop
       
        if game.guess in game.mystery_word_list:
        #if the guessed letter is in the mystery word
            indices = [i for i, letter in enumerate(game.mystery_word_list) if letter == game.guess]
            #finds all indices where guessed letter is in mystery word
            for i in indices:
                game.guessed_word[i] = game.guess
                #updates the guessed word list to reflect the correctly guessed letter
            print("\nSuccessful guess!")
            drawing(game.life_counter)   
        else:
            game.life_deductor(1)
            #deducts one life from player if guess is incorrect
            print("\nSorry wrong guess!")
            drawing(game.life_counter)
            if game.life_counter == 1:
                print("You have 1 life left.\n")
            else:
                print("You have {} lives left.\n".format(game.life_counter))
            #displays lives left

    # Determine if player won or lost
    if game.life_counter == 0:
        print("You lost!\nThe correct word was '{}'".format(game.mystery_word))
    else:
        print("You win!\nYou guessed the word '{}' correctly!".format(game.mystery_word))
        
if __name__ == "__main__":
    play_hangman()
