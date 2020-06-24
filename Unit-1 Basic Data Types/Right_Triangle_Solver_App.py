#Python Challenge 4	Right Triangle Solver App
import math

#Get User Input
print("Welcome to the Right Triangle Solver App")

first_leg = float(input("\nWhat is the first leg of the triangle: "))
second_leg = float(input("What is the second leg of the triangle: "))

hypo = math.sqrt(first_leg**2 + second_leg**2)
hypo = round(hypo, 3)

area = 1/2 * first_leg * second_leg
area = round(area, 3)

print("\nFor a triangle with legs of " + str(first_leg) + "and" + str(second_leg) + " the hypotenuse is " + str(hypo) + ".")
print("For a triangle with legs of " + str(first_leg) + "and" + str(second_leg) + " the area is " + str(area) + ".")