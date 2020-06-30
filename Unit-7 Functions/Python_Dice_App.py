# Python Challenge 31	Python Dice App

import random

def dice_sides():
	side = int(input("\nHow many sides would you like on your dice: "))
	return side	
		
def dice_number():
	dice = int(input("How many dice would you like to roll: "))
	return dice
	
def game(side, dice):
	print("\nYou rolled " + str(dice) + " " + str(side) + " sided dice.")
	print("\n-----Results are as followed-----")
	
	sides = []
	rand_ch = []	
	
	for s in range(1, side+1):
		sides.append(s)
		
	for d in range(1,dice+1):
		r_ch = random.choice(sides)
		rand_ch.append(r_ch)	
		print("\t" + str(r_ch))
	
	return rand_ch
		
def sum_dice(rand_ch):		
	print("The total value of your roll is " + str(sum(rand_ch)) + ".")
	
def roll_again():
	play_again = input("\nWould you like to roll again (y/n): ").lower()
	
	if play_again != 'y':
		roll = False
	else:
		roll = True
	return roll


print("Welcome to the Python Dice App\n")
playing = True
while playing:
	d_sides = dice_sides()
	d_number = dice_number()

	my_dice = game(d_sides, d_number)
	sum_dice(my_dice)

	playing = roll_again()

print("Thank you for using the Python Dice App.")