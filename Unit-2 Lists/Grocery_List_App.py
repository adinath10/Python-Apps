#Python Challenge 8	Different Types of Lists Program

import datetime as dt
import time as tm

dtnow = dt.datetime.fromtimestamp(tm.time())
#OR
'''
time = dt.dt.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
'''

print("Welcome to the Grocery List App.")

print("Current Date and Time: " + str(dtnow.day) + "/" + str(dtnow.month) + "\t" + str(dtnow.hour) + ":" + str(dtnow.minute))

grocery = ['Meat','Cheese']

print("You currently have " + str(grocery[0]) + " and " + str(grocery[1]) + " in your list.")

groc = input("\nType of food to add to the grocery list: ").title().strip()
grocery.append(groc)
groc = input("Type of food to add to the grocery list: ").title().strip()
grocery.append(groc)
groc = input("Type of food to add to the grocery list: ").title().strip()
grocery.append(groc)

print("\nHere is your grocery list:\n" + str(grocery))
grocery_sort = sorted(grocery)
print("Here is your list sorted:\n" + str(grocery_sort))

print("\nSimulating grocery shopping...")

print("\nCurrent grocery list: " + str(len(grocery_sort)) + " items\n" + str(grocery_sort))
groc_remove = input("what food did you just buy: ").title().strip()
grocery_sort.remove(groc_remove)
print("Removing " + str(groc_remove) + " from list...")

print("\nCurrent grocery list: " + str(len(grocery_sort)) + " items\n" + str(grocery_sort))
groc_remove = input("what food did you just buy: ").title().strip()
grocery_sort.remove(groc_remove)
print("Removing " + str(groc_remove) + " from list...")

print("\nCurrent grocery list: " + str(len(grocery_sort)) + " items\n" + str(grocery_sort))
groc_remove = input("what food did you just buy: ").title().strip()
grocery_sort.remove(groc_remove)
print("Removing " + str(groc_remove) + " from list...")

print("\nCurrent grocery list: " + str(len(grocery_sort)) + " items\n" + str(grocery_sort))

print("\nSorry, the store is out of " + str(grocery_sort[1] + "."))
groc_replace = input("What food would you like instead: ").title().strip()
grocery_sort[1] = groc_replace

print("\nHere is what remains on your grocery list:\n" + str(grocery_sort))