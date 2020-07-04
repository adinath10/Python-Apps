#Python Challenge 34	Head to Head Tic Tac Toe App

def draw_board(char_list):
	print("\n\t    Tic-Toc-Toe")
	print("\t--------------------")
	print("\t|| " + char_list[0] + " || " + char_list[1] + " || " + char_list[2] + " ||")
	print("\t|| " + char_list[3] + " || " + char_list[4] + " || " + char_list[5] + " ||")
	print("\t|| " + char_list[6] + " || " + char_list[7] + " || " + char_list[8] + " ||")
	print("\t--------------------")

def get_player_input(player_char, char_list):
	while True:
		player_move = int(input(player_char + ": Where would you like to place your piece (1-9): "))
		if player_move > 0 and player_move < 10:
			if char_list[player_move - 1] == '_':
				return player_move
			else:
				print("That spot has already been chose. Try again.")
		else:
			print("That is not a spot on the board.	Try again.")

def place_char_on_board(player_char, player_move, char_list):
	char_list[player_move - 1] = player_char

def is_Winner(pC, cL):
	return ((cL[0] == pC and cL[1] == pC and cL[2] == pC) or
		(cL[3] == pC and cL[4] == pC and cL[5] == pC) or
		(cL[6] == pC and cL[7] == pC and cL[8] == pC) or
		(cL[0] == pC and cL[3] == pC and cL[6] == pC) or
		(cL[1] == pC and cL[4] == pC and cL[7] == pC) or
		(cL[2] == pC and cL[5] == pC and cL[8] == pC) or
		(cL[0] == pC and cL[4] == pC and cL[8] == pC) or
		(cL[2] == pC and cL[4] == pC and cL[6] == pC))

player_1 = 'X'
player_2 = 'O'
n_list = ['1','2','3','4','5','6','7','8','9']
c_list = ['_']*9

draw_board(n_list)
draw_board(c_list)

while True:
	move = get_player_input(player_1, c_list)
	place_char_on_board(player_1, move, c_list)

	draw_board(n_list)
	draw_board(c_list)

	if is_Winner(player_1, c_list):
		print("Player 1 wins!")
		break

	elif "_" not in c_list:
		print("The game was a tie!")
		break

	
	move = get_player_input(player_2, c_list)
	place_char_on_board(player_2, move, c_list)

	draw_board(n_list)
	draw_board(c_list)

	if is_Winner(player_2, c_list):
		print("Player 2 wins!")
		break



