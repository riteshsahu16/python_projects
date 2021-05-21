 
# Welcome to Kaun Banega Crorepati

## About
  Welcome this is the next step in the process, prerequisites for this task are a basic understanding of python to solve this and then of git.

  If you are new to the language use this to python 3 https://www.learnpython.org/, Learn the Basics should be sufficent for this task.

  Next step is to Install python3 in your local and jump to the task.

  About the task 

  In this task we will code Kaun Banega Crorepati. The idea behind is to make ourselves familiar with python language. It will be your first project. You can add extra features if you want. 
  
  It's like a quiz game where there will be 15 questions asked from user. Every question has one correct answer. They can also go for lifelines. At the end you will display the results how much the user earned. Perform following tasks to complete the game.
  
### SETUP THE GAME CODE.

  *  Install git
  * `git clone https://github.com/devs-nest/kbc.git`
  * `python kbc.py` (to run code, you would be using python3) 

---
### List of Tasks ( Complete kbc function ):
  ### Task 1 (Setting up)
  
  * Open the `kbc.py` 
  * Read the comments inside kbc function and read the code, to understand you can also use a debugger.
  * Modify the code accordingly.
  * Fix the isAnswerCorrect function to return true whenever the answer is right or false otherwise
  ### Task 2 (LOOPING)
  
  When you run this program it will only take the user's input once and then it will stop
  * You have to take multiple inputs from the user, use a loop for this that iterates over a list of all 15 questions.
  * Statements like "welcome to the game" should only be printed once, take note of this. You can add statements if you want
  
  ### Task 3 (SET MINIMUM REWARD ACCORDING TO THE Level(Padaav))
  
  If the user is:

  * below questions number 6, then the minimum amount rewarded is Rs. 0 (zero)
  * As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First Level)
  * As he correctly answers question number 10, the minimum reward becomes Rs. 3,20,000 (Second Level)

  ### Task 4 (LIFELINE)

  There is a 50-50 life-line where two incorrect options get disappeared

  * 50-50 lifeline can be used ONLY ONCE.
  * There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
  
  ### TASK 5 (QUIT)
  
  If the user inputs "quit" (case insensitive) as input, then user returns with the amount he/she has won until now,
	instead of the minimum amount.
 
  ```
  
  
  ### TESTING
  * Go to questions.py and add 15 different questions to the list in JSON format.
  * Test your code with multiple inputs to see if it works fine


  ### Pushing your code
    Once you have solved it in your local, push it to a private repo and message us that you have solved it, Also don't forget to add usernames: [“vedansh”, “prachipathrayan”] as collaborators

  


