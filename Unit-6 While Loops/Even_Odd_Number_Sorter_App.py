#Python Challenge 27	Even Odd Number Sorter App

print("Welcome to the Even Odd Number Sorter App")

running = True

while running:
	number = input("\nEnter in a string of numbers separated by a comma (,) : ").replace(' ','').split(',')
	
	even = []
	odd = []
	
	print("\n---- Result Summary ----")

	for num in number:
		num = int(num)
		if num%2 == 0:
			print("\t" + str(num) + " is even!")
			even.append(num)
		else:
			print("\t" + str(num) + " is odd!")
			odd.append(num)

	print("\nThe following " + str(len(even)) + " numbers are even:")
	even.sort()
	for e in even:
		print("\t" + str(e))

	print("\nThe following " + str(len(odd)) + " numbers are odd:")
	odd.sort()
	for o in odd:
		print("\t" + str(o))

	choice = input("\nWould you like to run the program again (y/n): ").lower().strip()
	if choice != 'y':
		print("Thank you for using the program.	Goodbye.")
		running = False 