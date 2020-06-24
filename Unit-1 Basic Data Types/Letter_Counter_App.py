#Python Challenge 1	Letter Counter App

print("Welcome to the Letter Counter App")

#Get User Input
name = input("\nWhat is your name: ").title().strip()
print("Hello, " + name.title() + "!")

print("I will count the number of times that a specific letter occurs in a message.")
msg = input("\nPlease enter a message: ")
figure_out = input("Which letter would you like to count the occurrences of: ")

#Standardrize to lower case
msg = msg.lower()
figure_out = figure_out.lower()

#Get the Count and Display Results 
letter_count = msg.count(figure_out)
print(f"\n{name.title()}, your message has {letter_count} {figure_out}'s in it")