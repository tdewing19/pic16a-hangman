# PIC 16A Hangman Project

**by:** Arely Aguirre, Tristan Dewing

## Description:

This project is a variation of the popular word game Hangman, which involves a player guessing the letters of a mystery word. The player is given 6 lives, meaning they are allowed 6 incorrect guesses before losing. If the player guesses all letters correctly before guessing 6 incorrectly, they win. The player is also allowed to guess the entire mystery word at once, allowing them the chance to win the game in one turn. However, if they guess the word incorrectly, they automatically lose the game.

## Instructions:

To run the hangman game yourself first clone this repository on your local computer using the following line:

```
git clone https://github.com/tdewing19/pic16a-hangman.git && cd pic16a-hangman
```

To install the package requirements on your local computer, use the following line:

```
conda create --name NEWENV --file requirements.txt
```

Then finally to try out the demo file, use the following line:

```
python main.py
```

## Demo File Description:




## Scope and Limitations:

The words in this game are currently limited to the 832 words from the `words.txt` file used in the project, and do not encompass all possible words in the English dictionary, notably excluding acronyms, proper nouns, and words with punctuation marks such as apostrophes and hyphens. This game is also built for the player to have exactly 6 lives, no less and no more. Hopefully this game can be expanded in the future to be able to handle a larger variety of words and adjust the number of lives the player can start out with.

## Dataset Source:

The `words.txt` file used in this project is based off of a hangman word file found at the following site:

```
https://github.com/Xethron/Hangman/blob/master/words.txt
```
The `words.txt` file used in our project includes all words that are contained in the file from the website above, except those that are capitalized or are less than three letters.

## Tutorial Used:

Our project was inspired by `Problem Set 2` found at:

```
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/
```
Our project builds upon the tutorial by including:
  1. The ability for users to guess words
  2. The ability for users to confirm their guess if they guessed more than one letter at a time
  3. A function that prints different hangman drawings depending on the number of lives the user has

## Acknowledgement:

Thank you to Professor Harlin, as well as our TA Shruti and LA's Mansa and Jaya for your help and guidance throughout the quarter!
