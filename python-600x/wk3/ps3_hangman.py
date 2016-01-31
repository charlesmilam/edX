# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
# -----------------------------------
# Sample output
# Loading word list from file...
# 55900 words loaded.
# Welcome to the game, Hangman!
# I am thinking of a word that is 4 letters long.
# -------------
# You have 8 guesses left.
# Available letters: abcdefghijklmnopqrstuvwxyz
# Please guess a letter: a
# Good guess: _ a_ _
# ------------
# You have 8 guesses left.
# Available letters: bcdefghijklmnopqrstuvwxyz
# Please guess a letter: a
# Oops! You've already guessed that letter: _ a_ _
# ------------
# You have 8 guesses left.
# Available letters: bcdefghijklmnopqrstuvwxyz
# Please guess a letter: s
# Oops! That letter is not in my word: _ a_ _
# ------------
# You have 7 guesses left.
# Available letters: bcdefghijklmnopqrtuvwxyz
# Please guess a letter: t
# Good guess: ta_ t
# ------------
# Congratulations, you won!
# Sorry, you ran out of guesses. The word was else.

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_display = []

    for char in secretWord:
        if char in lettersGuessed:
            word_display.append(char)
        else:
            word_display.append('_')

    return ' '.join(word_display)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avail_letters = []
    for char in string.ascii_lowercase:
        avail_letters.append(char)

    for char in lettersGuessed:
        if char in avail_letters:
            avail_letters.remove(char)

    return ''.join(avail_letters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Welcome to the game, Hangman!
    # I am thinking of a word that is 4 letters long.
    num_guesses = 8
    letters_guessed = []
    guess = ''
    div = '-------------'
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print 'secret word', secretWord
    print div

    # You have 8 guesses left.
    # Available letters: abcdefghijklmnopqrstuvwxyz
    # Please guess a letter: a
    # Good guess: _ a_ _
    # ------------
    while num_guesses >= 0:
        print 'You have ' + str(num_guesses) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(letters_guessed)

        guess = raw_input('Please guess a letter: ').lower()
        letters_guessed.append(guess)

        if isWordGuessed(secretWord, letters_guessed):
            print div
            print 'Congratulations, you won!'
            break
        elif num_guesses == 1:
            num_guesses -= 1
            print div
            print 'Sorry, you ran out of guesses. The word was ' + secretWord
            break
        else:
            num_guesses -= 1







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
