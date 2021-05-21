import random



def load_words():
    """
    this function help to load more word by updating word_list (list)    
    Example :-
        word_list = ["learning", "kindness", "joy", "kiet", "good"] (old)
        word_list = ["learning", "kindness", "joy", "kiet", "good" ,"hello"] (new)
    """
    word_list = ["learning", "kindness", "joy", "kiet", "good"]

    # uncomment the below for testing
    word_list = []
    #WORDLIST_FILENAME = "words.txt"
    #inFile = open(WORDLIST_FILENAME, 'r')
    #line = inFile.readline()
    #word_list = string.split(line)

    #readlines: returns list of lines
    #each element will contain a line
    #split
    count = 5
    with open("words.txt", "r") as file:
        data = file.readlines()
        for line in data:
            if(count == 0):
                break
            word_list = line.split(' ')
            count -= 1
    return word_list


def choose_word():
    """
    word_list (list): list of words (strings)
    this function return one random world from list
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
