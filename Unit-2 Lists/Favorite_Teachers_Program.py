#Python Challenge 10	Favorite Teachers Program

print("Welcome to the Favorite Teachers Program")

teacher = []

mam = input("\nWho is your first favorite teacher: ").title().strip()
teacher.append(mam)
mam = input("Who is your second favorite teacher: ").title().strip()
teacher.append(mam)
mam = input("Who is your third favorite teacher: ").title().strip()
teacher.append(mam)
mam = input("Who is your forth favorite teacher: ").title().strip()
teacher.append(mam)

print("\nYour favorite teachers ranked are:", teacher)
teacher_sort = sorted(teacher)
print("Your favorite teachers alphabetically are:", teacher_sort)
teacher_revsort = sorted(teacher, reverse = True) 
print("Your favorite teachers in reverse alphabetically order are:", teacher_revsort)

print("\nYour top two teachers are: " + str(teacher[0]) + " and " + str(teacher[1]) + ".")
print("Your next two favorite teachers are: " + str(teacher[2]) + " and " + str(teacher[3]) + ".")
print("Your last favorite teachers is: " + str(teacher[-1]) + ".")
print("You have a total of " + str(len(teacher)) + " favorite teachers.")

print("\nOops, " + str(teacher[0]) + " is no longer your first favorite teacher.", end = ' ')
new_mam = input("Who is your new FAVORITE teacher: ").title().strip()
teacher.insert(0, new_mam)

print("\nYour favorite teachers ranked are:", teacher)
teacher_sort = sorted(teacher)
print("Your favorite teachers alphabetically are:", teacher_sort)
teacher_revsort = sorted(teacher, reverse = True) 
print("Your favorite teachers in reverse alphabetically order are:", teacher_revsort)

print("\nYour top two teachers are: " + str(teacher[0]) + " and " + str(teacher[1]) + ".")
print("Your next two favorite teachers are: " + str(teacher[2]) + " and " + str(teacher[3]) + ".")
print("Your last favorite teachers is: " + str(teacher[-1]) + ".")
print("You have a total of " + str(len(teacher)) + " favorite teachers.")

print("\nYou've decided you no longer like a teacher.", end = ' ')
remove_mam = input("Which teacher would you like to remove from your list: ").title().strip()
teacher.remove(remove_mam)

print("\nYour favorite teachers ranked are:", teacher)
teacher_sort = sorted(teacher)
print("Your favorite teachers alphabetically are:", teacher_sort)
teacher_revsort = sorted(teacher, reverse = True) 
print("Your favorite teachers in reverse alphabetically order are:", teacher_revsort)

print("\nYour top two teachers are: " + str(teacher[0]) + " and " + str(teacher[1]) + ".")
print("Your next two favorite teachers are: " + str(teacher[2]) + " and " + str(teacher[3]) + ".")
print("Your last favorite teachers is: " + str(teacher[-1]) + ".")
print("You have a total of " + str(len(teacher)) + " favorite teachers.")