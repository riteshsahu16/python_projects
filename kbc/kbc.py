from questions import QUESTIONS
import random

def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == question["answer"] else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''

    #Make two option = "" other than correct return it
    ans = ques['answer']
    x = 0
    while True:
        x = random.randint(1,4)
        if x != ans:
            break
    for i in range(1,5):
        if i != ans and i != x:
            print(" i ", i)
            ques["option"+str(i)] = ""
    return ques

def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

    current_money = 0
    min_amount = 0
    lifeline_available = True
    ques = 0
    while ques < 15:
    

        print(f'\tQuestion {ques+1}: {QUESTIONS[ques]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[ques]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[ques]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[ques]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[ques]["option4"]}')
        ans = input(f'Your choice ( 1-4 ) (quit) (lifeline-available: {lifeline_available} ) :  ')

        # check for the input validations
        if ans.lower() == 'quit':
            break


        if ans.lower() == 'lifeline' and lifeline_available==True and ques !=14:
            #logic for lifeline
            lifeline_available = False
            current_ques = lifeLine(QUESTIONS[ques])
            print(f'\tQuestion {ques+1}: {QUESTIONS[ques]["name"]}' )
            print(f'\t\tOptions:')
            print(f'\t\t\tOption 1: {QUESTIONS[ques]["option1"]}')
            print(f'\t\t\tOption 2: {QUESTIONS[ques]["option2"]}')
            print(f'\t\t\tOption 3: {QUESTIONS[ques]["option3"]}')
            print(f'\t\t\tOption 4: {QUESTIONS[ques]["option4"]}')
            ans = input('Your choice ( 1-4 ) (quit): ')
        
        elif ans.lower() == 'lifeline' and (lifeline_available==False or ques ==14):
            print("* * * Lifeline not available!!! * * *")
            continue

        if isAnswerCorrect(QUESTIONS[ques], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            if ques==4:
                min_amount = 10000
            elif ques==10:
                min_amount = 320000
            current_money += QUESTIONS[ques]['money']

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            current_money = min_amount
            print()
            break

        print("current_money earned : ", current_money)
        print("minimum amount: ", min_amount)
        print()

        ques += 1
    # print the total money won in the end.
    print("Total Amount : ", current_money)

kbc()
