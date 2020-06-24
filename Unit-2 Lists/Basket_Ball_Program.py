#Python Challenge 9	Basketball Roster Program

print("Welcome to the Basketball Roster Program")

roster = []

player = input("\nWho is your point guard: ").title().strip()
roster.append(player)
player = input("Who is your point guard: ").title().strip()
roster.append(player)
player = input("Who is your small forward: ").title().strip()
roster.append(player)
player = input("Who is your power forward: ").title().strip()
roster.append(player)
player = input("Who is your center: ").title().strip()
roster.append(player)

print("\n\tYour starting  for the upcoming basketball season")
print("\t\tPoint Guard:\t\t", roster[0])
print("\t\tShooting Guard:\t\t", roster[1])
print("\t\tSmall Forward:\t\t", roster[2])
print("\t\tPower Forward:\t\t", roster[3])
print("\t\tCenter:\t\t\t", roster[4])

print("\noh no, " + roster[2] + " is injured.")
injured = roster.pop(2)
print("Your roster only has " + str(len(roster)) + " players.")
replacement = input("who will take " + injured + "'s spot: ").title().strip()
roster.insert(2, replacement)

print("\n\tYour starting  for the upcoming basketball season")
print("\t\tPoint Guard:\t\t", roster[0])
print("\t\tShooting Guard:\t\t", roster[1])
print("\t\tSmall Forward:\t\t", roster[2])
print("\t\tPower Forward:\t\t", roster[3])
print("\t\tCenter:\t\t\t", roster[4])

print("\nGood luck " + replacement + " you will do great!")
print("Your roster now has " + str(len(roster)) + " players.")