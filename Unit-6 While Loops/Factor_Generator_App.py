#Python Challenge 26	Factor Generator App

print("Welcome to the Factor Generator App")

running = True

while running:
	factor_number = int(input("\nEnter a number to determine all factors of that number: "))

	fact = 1
	facts = range(fact, factor_number + 1)
	fact_num = []
	print("\nFactors of " + str(factor_number) + " are:")
	while facts:
		if factor_number % fact == 0:
			print(fact)
			fact_num.append(fact)
		elif fact > factor_number:
			break 	
		fact += 1

	print("\nIn summary: ")
	for i in range(len(fact_num)//2):
		print(str(fact_num[i]) + " * " + str(fact_num[-i-1]) + " = " + str(factor_number))

	run_again = input("\nRun again (y/n): ").lower().strip()
	if run_again == 'y':
		running = True
	elif run_again == 'n':
		print("Thank you for using the program.	Have a great day.")
		running = False
	else:
		print("Please enter either a Y or N.	Better Luck Next time!!")
		running = False
				
	