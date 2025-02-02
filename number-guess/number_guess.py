import random
number = random.randint(1, 100) # auto gen numbers from 1 to 100

while True: #asking question infinitely
    guess = int(input("Guess the number (1 to 10): "))

    if guess == number:
        print("Congratulations!!! Your guess is correct.")
        break #break if the user guessed it right
    else:
        print("Wrong guess!!! Try again")