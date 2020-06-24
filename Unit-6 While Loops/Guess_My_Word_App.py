#Python Challenge 29	Guess My Word App

import random

print("Welcome to the Guess My Word App")

game_dict = {
	"sports" : ['basketball', 'baseball', 'soccer', 'football', 'tennis', 'curling'],
	"colors" : ['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
	"fruits" : ['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
	"classes" : ['english', 'history', 'science', 'mathematics', 'art', 'health'],
	}

game_keys = []
for key in game_dict.keys():
	game_keys.append(key)
	
playing = True
while playing:
	game_category = random.choice(game_keys)
	game_word = random.choice(game_dict[game_category])

	blank_word = []
	for letter in game_word:
		blank_word.append("-")
	
	print("\nGuess a " + str(len(game_word)) + " letter word from the following category: " + game_category.title())	
	
	guess = ""
	guess_count = 0
	
	while guess != game_word:
		print("".join(blank_word))
		guess = input("\nEnter your guess: ").lower().strip()
		guess_count += 1

		if guess == game_word:
			print("\nCorrect!   You guessed the word in " + str(guess_count) + " guesses.")
			break
			
		else:
			print("That is not correct . let us reveal a letter to help you!")
			swapping = True
			while swapping:
				letter_index = random.randint(0, len(game_word) - 1)
				if blank_word[letter_index] == "-":
					blank_word[letter_index] = game_word[letter_index]
					swapping = False
			
	choice = input("\nWould you like to play again (y/n): ").lower()
	if choice != 'y':
		playing = False
		print("Thank you for playing the game.")