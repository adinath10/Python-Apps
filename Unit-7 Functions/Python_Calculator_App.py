# Python Challenge 32	Python Calculator App

def first_number():
	number_1 = float(input("\nEnter a number: "))
	return number_1

def second_number():
	number_2 = float(input("Enter a number: "))
	return number_2
	
def operation(number_1, number_2):
	oper = int(input("Enter an operations (1.addition, 2.subtraction, 3.multiplication, 4.division, or 5.exponentiation): "))
	return oper

def perform(oper, number_1, number_2):
	if oper == 1:
		add = number_1 + number_2	 
		print("The sum of " + str(number_1) + " and " + str(number_2) + " is " + str(add) + ".")	
		return add
	
	elif oper == 2:
		subtract = number_1 - number_2
		print("The difference of " + str(number_1) + " and " + str(number_2) + " is " + str(subtract) + ".")
		return subtract

	elif oper == 3:
		multiply = number_1 * number_2
		print("The Product of " + str(number_1) + " and " + str(number_2) + " is " + str(multiply) + ".")
		return multiply	

	elif oper == 4:
		if number_2 == 0:
			divide = "DIV ERROR"
			print("You cannot divide by zero.")
			return divide		
		else:
			divide = number_1/number_2
			print("The quotient of " + str(number_1) + " and " + str(number_2) + " is " + str(divide) + ".")
			return divide	
	
	elif oper == 5:
		expo = number_1 **number_2
		print("The result of " + str(number_1) + " raised to the " + str(number_2) + " is " + str(expo) + ".")
		return expo
	
	else:
		print("That is not a valid operation.	Try again.")
		opp = "OPP ERROR"
		return opp
	
def play_again():
	choice = input("Would you like to run the program again (y/n): ")
	if choice != 'y':
		play = False
	else:
		play = True
	return play
		

playing = True

print("Welcome to the Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed.")

while playing:
	f_number = first_number()
	s_number = second_number()

	operation_no = operation(f_number, s_number)
	perform_opr = perform(operation_no, f_number, s_number)

	playing = play_again()

print("\nThank you for using the Python Calculator App.   Goodbye.")

	