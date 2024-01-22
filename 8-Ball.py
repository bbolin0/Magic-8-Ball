#Bobo Lin
#1/22/2024
#Magic 8-Ball

import random

#generates a response based on question from user
#no parameters
def eightBall():
    #list of responses
    responses = [
            'Most definitely', 
             'Ask again later',
             'Without a doubt', 
             'My sources say no', 
             'Cannot predict now',
             'Very doubtful', 
             'As I see it, yes', 
             'Concentrate and ask again', 
             'It is certain', 
             'Reply hazy, try again' 
    ]

    #prints eight ball pic
    print('''
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⡿⠟⣉⣡⣤⣴⣶⣶⣶⣶⣦⣤⣌⣉⠻⢿⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⠟⢁⣴⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿
            ⣿⣿⣿⡿⢁⣴⡟⠁⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿
            ⣿⣿⡟⢡⣿⠏⠀⠀⢠⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠉⠙⠻⣿⣿⣿⡌⢻⣿⣿
            ⣿⣿⠁⣾⠏⠀⠀⣰⣿⣿⣿⣿⣿⡿⠁⠀⠀⢠⡤⠤⣤⠀⠀⠘⢿⣿⣷⠈⣿⣿
            ⣿⡇⢰⣿⠀⠀⢰⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠸⣄⣀⣟⠀⠀⠀⠘⣿⣿⡆⢸⣿
            ⣿⡇⢸⣿⠀⢠⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⢠⡏⠀⠈⣷⠀⠀⢠⣿⣿⡇⢸⣿
            ⣿⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠻⠶⠞⠃⠀⢀⣾⣿⣿⠇⢸⣿
            ⣿⣿⡀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⢀⣠⣴⣿⣿⣿⡿⢀⣿⣿
            ⣿⣿⣧⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣼⣿⣿
            ⣿⣿⣿⣷⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣾⣿⣿⣿
            ⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣷⣦⣉⡙⠛⠻⠿⠿⠿⠿⠟⠛⢋⣉⣴⣾⣿⣿⣿⣿⣿⣿⣿
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ''')

    #prints welcome message
    print('Welcome to Magic 8 Ball!')

    #asks user for question
    question = input('Enter your question with a question mark. ')

    #validates if question ends with a question mark
    #if not, prompts the user to re-enter the question with a question mark
    #recalls function and repeats
    if not question.endswith('?'):
        print('Your input does not seem to be a question. Please re-enter question. ')
        eightBall()
    #if yes
    #prints a random response from the response list
    #asks user if they want to ask another question
    #if yes, recall function
    #if no, quit function
    else:
        print(random.choice(responses))
        again = input('Would you like to ask another question? Please enter yes or no. ')
        if again == 'yes':
            eightBall()
        else:
            quit()

#Main
eightBall()