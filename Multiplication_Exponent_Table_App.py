#Basic Data Types Challenge 5	Multipication/Exponent Table App

print("Welcome to the Multiplication/Exponent Table App")

name = input("\nHello, what is your name: ").title().strip()

number = input("What number would you like to work with: ")

print("Multiplication Table for ", number)

print("1.0 * " + str(number) + " = " + str(round(1*number, 4)))
