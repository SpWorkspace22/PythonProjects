'''Dice Rolling Simulation '''


import random 

def DiceRolling():

    while True:
        
        rolled = random.randint(1,6)
        print(f'******Rolled {rolled} *********',end="\n")

        response = input("Roll Again Yes or No")
        if response == "No":
            break

DiceRolling()
