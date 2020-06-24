#Python Challenge 6	Grade Sorter App

print("Welcome to the Grade Sorter App")

grades = []

grade = int(input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your second grade (0-100): "))
grades.append(grade)
grade = int(input("What is your third grade (0-100): "))
grades.append(grade)
grade = int(input("What is your fourth grade (0-100): "))
grades.append(grade)

print("\nYour grades are:", grades)

grade_sort = sorted(grades, reverse = True)

print("\nYour grades from highest to lowest are:", grade_sort)

print("\nThe lowest two grades will now be dropped.")

grade_removed_1 = grade_sort.pop()
grade_removed_2 = grade_sort.pop()
print("Removed grade:", grade_removed_1)
print("Removed grade:", grade_removed_2)

print("\nYour remaining grades are:", grade_sort)
print("Nice work!   Your highest grade is a " + str(grade_sort[0]) + ".")