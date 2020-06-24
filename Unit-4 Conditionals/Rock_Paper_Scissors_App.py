#Python Challenge 20	Rock, Paper, Scissors App

import random
print("Welcome to a game of Rock, Paper, Scissors")

rounds = int(input("\nHow many rounds would you like to play: "))

Player = 0
Computer = 0

for r in range(1,rounds+1):
	
	print("Round", r)
	print("Player: " + str(Player) + "\tComputer: " + str(Computer))
	Equip = ['rock', 'paper', 'scissors']
	C_pick = random.choice(Equip)
	P_pick = input("Time to pick...rock, paper, scissors: ").lower().strip()
	print("\tComputer: ", C_pick)
	print("\tPlayer: ", P_pick)

	if P_pick in Equip:
		if P_pick == 'rock' and C_pick == 'rock':
			print("\tIt is a tie, how boring!")
			print("\tThis round was a tie.\n")
		elif P_pick == 'paper' and C_pick == 'rock':
			Player += 1
			print("\tPaper covers Rock!")
			print("\tYou win round " + str(r) + ".\n")
		elif P_pick == 'scissors' and C_pick == 'rock':
			Computer += 1
			print("\tRock smashes Scissors!")
			print("\tComputer wins round " + str(r) + ".\n")	
			

		if P_pick == 'rock' and C_pick == 'paper':
			Computer += 1
			print("\tPaper covers Rock!")
			print("\tComputer wins round " + str(r) + ".\n")
		elif P_pick == 'paper' and C_pick == 'paper':
			print("\tIt is a tie, how boring!")
			print("\tThis round was a tie.\n")
		elif P_pick == 'scissors' and C_pick == 'paper':
			Player += 1
			print("\tScissors cut paper!")
			print("\tYou win round " + str(r) + ".\n") 	
		 

		if P_pick == 'rock' and C_pick == 'scissors':
			Player += 1
			print("\tRock smashes Scissors!")
			print("\tYou win round " + str(r) + ".\n")
		elif P_pick == 'paper' and C_pick == 'scissors':
			Computer += 1
			print("\tScissors cut paper!")
			print("\tComputer wins round " + str(r) + ".\n")
		elif P_pick == 'scissors' and C_pick == 'scissors':
			print("\tIt is a tie, how boring!")
			print("\tThis round was a tie.\n")
	else:
		Computer += 1
		print("That is not a valid option!")
		print("Computer gets the point\n") 

	
print("Final Game Results")
print("\tRounds Played:", rounds)
print("\tPlayer Score:", Player)
print("\tComputer Score:", Computer)

if Player > Computer:
	print("\nWinner: You Win :-) !!!")
elif Computer > Player:
	print("\nWinner: Computer :-(")
else:
	print("\nThe Game was a Tie.")
 