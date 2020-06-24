#Python Challenge 12	Quadratic Solver App

import cmath

print("Welcome to the Quadratic Solver App.")

print("\nA quadratic is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

max_value = int(input("\nHow many equations would you like to solve today: "))
no_of_equations = range(1, max_value+1)
for num in no_of_equations:
	print("\nSolving equation #" + str(num))
	print("-----------------------------------------------------------------")
	
	a = float(input("\nPlease enter your value of a (coefficent of x^2): "))
	b = float(input("Please enter your value of b (coefficent of x): "))
	c = float(input("Please enter your value of c (coefficent): "))
	
	x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
	x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
	 
	print("\nThe solutions to " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " are:")
	print("\n\tx1 = " + str(x1))
	print("\tx2 = " + str(x2) )

print("\nThank you for using the Quadratic Solver App.	Goodbye.")

