#Python Challenge 15	Average Calculator App

print("Welcome to the Grade Point Average Calculator App")

name = input("What is your name: ").title().strip()

grades = []
number = int(input("How many grades would you like to enter: "))

for num in range(1, number + 1):
	num = int(input("Enter grade: "))
	grades.append(num)

grades.sort(reverse = True)	
print("\nGrades Highest to Lowest: ")
for grade in grades:
	print("\t" + str(grade))

average = sum(grades) / len(grades)
average = round(average, 2)

print("\n" + name + "'s Grade Summary:" )
print("\tTotal Number of Grades:", number)
print("\tHighest Grade:", max(grades))
print("\tLowest Grade:", min(grades))
print("\tAverage:", str(average))

desired_avg = float(input("\nWhat is your desired average: "))
grade_req = desired_avg*(len(grades) + 1) - sum(grades)
grade_req = round(grade_req, 2)

print("\nGood luck " + name + "!")
print("You will need to get a " + str(grade_req) + " on your next assignmentto earn a " + str(desired_avg) + " average.")

new_grades = grades[:]
print("\nLets see what you average could have been if you did better/worse on an assignment.")
grade_change = int(input("What grade would you like to change: "))
new_grades.remove(grade_change)
new_grade = int(input("What grade would you like to change " + str(grade_change) + " to : "))
new_grades.append(new_grade)

new_grades.sort(reverse = True)	
print("\nGrades Highest to Lowest: ")
for grade in new_grades:
	print("\t" + str(grade))

new_average = sum(new_grades) / len(new_grades)
new_average = round(new_average, 2)

print("\n" + name + "'s New Grade Summary:" )
print("\tTotal Number of Grades:", new_grades)
print("\tHighest Grade:", max(new_grades))
print("\tLowest Grade:", min(new_grades))
print("\tAverage:", str(new_average))

print("\nYour new average would be a " + str(new_average) + " compared to your real average of " + str(average) + " !")
average_change = new_average - average
average_change = round(average_change, 2)
print("This is change of " + str(average_change) + " points!")

print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go ask for extra credit!")