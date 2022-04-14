# A progrrame that will generate a random number between 0 to 100 
# User will guess the number and will check wheather he is correct or not


import random

def NumberGuess():
    attempt = 3

    #Random Number between 0 to 100
    number = random.randint(0,100)

    #user input
    print('-------------Guess the Number (3 Attempts only)-----------------------')
    while attempt>0:
        guess = int(input('Enter your guess '))
        if guess==number:
            print('You hit a jackpot',end="\n")
        else:
            attempt = attempt -1
            print(f'Try Again {attempt} left')
    else:
        print('---------You Lost the game--------------------------------')
    

NumberGuess()