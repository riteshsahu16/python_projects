import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    is_right = True
    for i in letters_guessed:
        if i not in secret_word:
            is_right = False
            break
    if is_right:
        return True
    return False

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    for i in letters_left:
        if i in letters_guessed:
            letters_left = letters_left.replace(i, '')
    return letters_left


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []

    max_tries = len(set(secret_word))
    wrong_count = 0
    guessed = ""

    while wrong_count < len(IMAGES):
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))
        print()
        if(len(guessed)) > len(secret_word) :
            break
        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if letter not in available_letters:
            print(letter," is not available !!!")
            print()
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
            guessed = get_guessed_word(secret_word, letters_guessed)
            print("Good guess: {} ".format(
                guessed))
            print()
            
        else:
            guessed = get_guessed_word(secret_word, letters_guessed)
            print("Oops! That letter is not in my word: {} ".format(
                guessed))
            letters_guessed.append(letter)
            print(IMAGES[wrong_count])
            wrong_count += 1
            print("")
        if(guessed.replace('_', '') == secret_word):
            break
    if guessed == secret_word:
        print(" * * Congratulations, you won! * * ", end='\n\n')
    else:
        print("* * * Sorry. You lost * * *", end='\n\n')

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
#print("secret_word ", secret_word)
print()

hangman(secret_word)
