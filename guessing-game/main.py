# THE PERFECT GUESS

import random

computer = random.randint(1, 10)   # store random number

def game():  # main function
    guess = 0
    while True:  # infinite loop
        try:
            number = int(input("Guess Number: ")) # if input is int. its good. move forward.
        except ValueError:
            print("Kindly choose in mathematical numbers.")   # if not. print this and...
            continue  # go back to asking again
        
        guess += 1  # every time its an int. increase the count
        if number == computer:     # if exact. 
            print("You won")    
            break                  # break
        elif number > computer:   # other conditions
            print("Guess a smaller number")
        else:
            print("Guess a higher number")
    
    print(f"You took {guess} guesses to choose the right number.")  # print along with guess.
    

while True:
    diff = input("Choose difficulty: Easy (e), Medium (m), Hard (h): ").lower()  # ask for difficulty

    if diff == "e":  # if e. choose from 1-10 
        computer = random.randint(1, 10)
        game()
        break    # and break

    elif diff == "m":  # same functionality as e
        computer = random.randint(1, 50)
        game()
        break

    elif diff == "h": # same functionality as e
        computer = random.randint(1, 100)
        game()
        break

    else:
        print("You can only choose between levels [e, m, or, h]")   # if users chooses int or float, etc... print that and "While true will ask again"

