import random

guess_range = 50
answer = random.randint(1, guess_range)

print("Welcome to the number guessing game!")
print("")

guess = ""
while guess != answer:
  userInput = input("Guess a number between 1 and "+str(guess_range)+": ")
  guess = int(userInput)
  
print("Congratulations! You guessed the correct number. You win!") 