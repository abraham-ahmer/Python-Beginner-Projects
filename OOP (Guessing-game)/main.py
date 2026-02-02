
import random 

class GuessGame:
    def __init__(self):
        self.correct_guess = random.randint(1,10)

    def attempt(self):
        count = 0
        while True:
            count += 1
            try:
                guess = int(input("Guess: "))
            except ValueError:
                print("kindly guess int not any other type.")
                continue


            if guess == self.correct_guess:
                print(f"You won. Took {count} attempts.")
                break
            
            elif (guess > self.correct_guess):
                print("You choose a higher number. Guess low!!!")
            
            elif (guess < self.correct_guess):
                print("You choosed a smaller number. Guess high!!!")

game = GuessGame()
game.attempt()
