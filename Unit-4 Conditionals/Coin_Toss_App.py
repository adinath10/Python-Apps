#Python Challenge 17	Coin Toss App

import random

print("Welcome to the Coin Toss App")

print("\nI will flip a coin a set number of times.")
coin_toss = ['HEADS', 'tails']

total_flip = int(input("How many times would you like me to flip the coin: "))

result = input("Would you like see the result of each flip (y/n): ") 

if result == 'y':
	
	print("\nFlipping!!!\n")
	heads = 0
	tails = 0

	for flip in range(total_flip):
		toss = random.choice(coin_toss)
		print(toss)
		
		if toss == 'HEADS':
			heads += 1
		else:
			tails += 1
	
		if heads == tails:
			print("At " + str(flip + 1) + " flips, the number of heads and tails were equal at " + str(heads) + " each.")
			 
	print("\nResult of Flipping A Coin " + str(total_flip) + " Times")

	head_per = (heads / total_flip)*100
	head_per = round(head_per, 2)
	tail_per = (tails / total_flip)*100
	tail_per = round(tail_per, 2)

	print("\nSide\t\tCount\t\tPercentage")
	print("Heads\t\t" + str(heads) + "/" + str(total_flip) + "\t\t" + str(head_per))
	print("tails\t\t" + str(tails) + "/" + str(total_flip) + "\t\t" + str(tail_per))

else:
	pass		