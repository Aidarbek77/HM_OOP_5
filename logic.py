import random


class Game:
    def __init__(self, min_number, max_number, max_attempts, starting_capital):
        self.min_number = min_number
        self.max_number = max_number
        self.max_attempts = max_attempts
        self.starting_capital = starting_capital
        self.capital = starting_capital

    def generate_random_number(self):
        return random.randint(self.min_number, self.max_number)

    def start(self):
        print(f"Welcome to Guess the Number Game!")
        print(f"Guess a number between {self.min_number} and {self.max_number}.")
        print(f"You start with {self.starting_capital} capital.")


        target_number = self.generate_random_number()
        attempts = 0

        while attempts < self.max_attempts:
            try:
                guess = int(input(f"Attempt #{attempts + 1}: Enter your guess: "))
            except ValueError:
                print("Please enter a valid number and reload the code or game. 'LuckyAI'")
                return

            if guess 3== target_number:
                self.capital *= 2
                print(f"Congratulations! You guessed the number {target_number}. Your capital is now {self.capital}.")
                break
            elif guess < target_number :
                print(f"Wrong guess. The number is near to {target_number + 3},but lower.")
            elif guess > target_number :
                print(f"Wrong guess. The number is near to {target_number - 3},but higher.")
            else:
                print(f"Congratulations! You guessed the number {target_number} Your capital is now {self.capital}.")
                self.capital -= 1
            attempts += 1

        if attempts == self.max_attempts:
            print(f"Game over! You've used all your attempts. Your final capital is {self.capital}.")
