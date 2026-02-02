# PROJECT: SNAKE, WATER, GUN GAME

import random

userChoice = input("Enter Your Choice (snake, water, or gun): ").lower()

options = ["snake", "water", "gun"]
computer = random.choice(options)

print(f"Computer's Choice: {computer}")
print(f"Your Choice: {userChoice}")


if computer == userChoice:
    print("Its a draw!!")

elif computer == "snake" and userChoice == "water":
    print("You lose.")

elif computer == "snake" and userChoice == "gun":
    print("you win!!!")


elif computer == "water" and userChoice == "snake":
    print("You win!!!")

elif computer == "water" and userChoice == "gun":
    print("you lose.")


elif computer == "gun" and userChoice == "snake":
    print("You lose!!!")

elif computer == "gun" and userChoice == "water":
    print("you win!!!")

else:
    print("Kindly choose only from snake, gun, and water")
