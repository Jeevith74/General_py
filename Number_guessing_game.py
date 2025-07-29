import random
import art

print(art.Gameguessinglogo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)

attempts = 0 
while True:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "hard":
        attempts = 5
        break
    elif level == "easy":
        attempts = 10
        break
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")


print(f"You have {attempts} attempts remaining to guess the number.")


def num_guess():
    global attempts

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            return  
        elif guess < random_number:
            print("Too Low.\nGuess again.")
        else:  
            print("Too High.\nGuess again.")

        attempts -= 1 

        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print("You've run out of guesses, you lose.")
            print(f"The number was {random_number}.")


num_guess()