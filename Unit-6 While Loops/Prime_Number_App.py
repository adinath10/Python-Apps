#Python Challenge 28	Prime Number App

import time as tm

running = True

while running:
	print("\nEnter 1 to determine if a specific number is prime.")
	print("Enter 1 to determine all prime numbers within a set range.")
	choice = int(input("Enter your choice 1 or 2: "))
	if choice == 1:
		number = int(input("\nEnter a number to determine if it prime or not: "))
		if number > 2:
			for num in range(2,number):
				if number%num == 0:
					print(str(number) + " is not prime!")
					break
				else:
					print(str(number) + " is prime!")
					break
			
		else:		
			print(str(number) + " is prime!")
	
	elif choice == 2:
		lower = int(input("\nEnter the lower bound of your range: "))
		upper = int(input("\nEnter the upper bound of your range: "))
		
		prime = []
		
		start_time = tm.time()
	
		for num in range(lower, upper + 1):
			
			if num > 1:
				primes = True
				for i in range(2, num):
					if num % i == 0:
						primes = False
						break
			else:
				primes = False

			if primes:
				prime.append(num)


		end_time = tm.time()

		delta_time = round(end_time - start_time, 4)
		
		print("\nCalculations took a total of " + str(delta_time) + " seconds.")
		print("The following numbers between " + str(lower) + " and " + str(upper) + " are prime")
		input("Press enter to continue.")
		
		for p in prime:
			print(p)
		
	else:
		print("\nThis is not a valid option.")
				
	choose = input("would you like to run the program again (y/n): ")
	if choose != 'y':
		running = False	
		print("Thank you for using program.	Have a nice day.")		