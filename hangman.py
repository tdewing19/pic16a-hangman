# Hangman.py
# By: Arely Aguirre, Tristan Dewing

import random

class Hangman:
    '''
      Determines, modifies and holds many variables 
      that are necessary for the hangman game,
      including the mystery word, number of lives
      left, and letter bank for all letters not
      previously used by the user
    '''
    
    def __init__(self, word_file):
        '''
          Chooses the mystery work from word_file and 
          sets instance variables necessary for hangman
          Arguments:
              word_file: txt file input that holds 
                         words for hangman
          Returns:
              None
        '''
        self.words = [word.strip() for word in word_file.readlines()]
        self.mystery_word = random.choice(self.words)
        self.mystery_word_list = list(self.mystery_word)
        self.life_counter = 6
        self.guess = ""
        self.guessed_word = ["_" for i in range(len(self.mystery_word))]
        self.guessed_letters = []
        self.letter_bank = list("{abcdefghijklmnopqrstuvwxyz}")
  
    def life_deductor(self, n):
        '''
          Decreases life_counter by an integer n
          Arguments:
              n: number of lives that will be deducted
          Returns:
              None
        '''
        self.life_counter -= n
  
    def guess_letters(self):
        '''
          Appends self.guess to a guessed letters list
          Arguments:
              None
          Returns:
              None
        '''
        self.guessed_letters.append(self.guess)

    def remove_guess(self):
        '''
          Removes self.guess from letter_bank
          which holds all letters that haven't
          been guessed yet
          Arguments:
              None
          Returns:
              None
        '''
        self.letter_bank.remove(self.guess)