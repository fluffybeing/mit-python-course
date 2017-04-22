# 6.00 Problem Set 3
# 
# Hangman game
#
# By Rahul Ranjan

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
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    a = []
    b = []
    c = []
    for i in range(len(secretWord)):
        c.append('_')
    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if(lettersGuessed[i] == secretWord[j]):
                a.append(j)
                b.append(lettersGuessed[i])            
    for l in range(len(a)):
        c[a[l]] = b[l]
    c = ' '.join(c)
            
    return c
        



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a = ''
    import string
    b = string.ascii_lowercase 
    for i in range(len(lettersGuessed)):
        a = a + lettersGuessed[i]
   
    return b.translate(None, a)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")

    guessesLeft = 8
    lettersGuessed = []
    b = ''
    while guessesLeft > 0 :
        
        print("You have " + str(guessesLeft) + " guesses left.")
    
        print("Available letters: " + str(getAvailableLetters(lettersGuessed)))
        a = raw_input("Please guess a letter: ")

        

        if a.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed += a.lower()

            if a.lower() in secretWord:
                print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
                b = b + a
            else:
                print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
                guessesLeft -= 1
                
        print("------------")
        if isWordGuessed(secretWord, lettersGuessed) == True :
            print("Congratulations, you won!")
            break
            

            
    if guessesLeft == 0:  
        print("Sorry, you ran out of guesses. The word was else. ")
        
    
    

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
