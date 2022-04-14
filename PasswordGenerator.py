'''Generating unique aplphanumeric pasword '''

import random

def generatePassword():
    CapitalAlphabets = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
    smallAlphabets ="abcdefghijklmnopqrstuvwxys"
    Numbers = "0123456789"
    special = "~!@#$%^&*()_+"

    passwordString = CapitalAlphabets+smallAlphabets+Numbers+special

    count = 8
    password = ""
    while count  > 0:
        password = password+passwordString[random.randint(0,len(passwordString)-1)]
        count=count-1
    else:
        print(f'Generated PAssword {password}')

generatePassword()
    