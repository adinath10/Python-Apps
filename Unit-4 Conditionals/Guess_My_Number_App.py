#Python Challenge 19	Guess My Number App

import random
print("Welcome to the Guess My Number App")

name = input("\nHello! What is your name: ").title().strip()
print("Well " + name + ", I am thinking of a number between 1 and 20.")

guess_no = random.randint(1, 20)

for guess_num in range(5):
	guess = int(input("\nTake a guess: "))
	
	if guess < guess_no:
		print("Your guess is too low")
	elif guess > guess_no:
		print("Your guess is too high")
	else:	
		break


if guess == guess_no:
	print("\nGood job, " + name + "!	You guessed my number in " + str(guess_num + 1) + " guesses!")
else:	
	print("\nGame over.  The number I was thinking of was", guess_no)