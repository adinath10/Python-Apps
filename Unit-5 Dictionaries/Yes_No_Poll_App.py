#Python Challenge 23	Yes or No Issue Polling App

print("Welcome to the Yes or No Issue Polling App")

issue = input("\nWhat is the yes or no issue you will be voting on today: ")
no_of_votes = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for polling results: ")

yes = 0
no = 0
results = {}

for i in range(no_of_votes): 
	name = input("\nEnter your full name: ").title().strip()
	if name in results.keys():
		print("Sorry, it seems that someone with that name has already voted.")
	else:
		print("Here is your issue: ", issue)
		poll = input("What do you think...yes or no: ").lower().strip()
		if poll == 'yes':
			yes += 1
		elif poll == 'no':
			no += 1
		else:
			print("That is not a yes or no answer, but okay...")
	
		results[name] = poll
		print("Thank you " + name + "!	Your vote of " + results[name] + " has been recorded.")		
	
print("\nThe following " + str(len(results.keys())) + " people voted: ")
for key in results.keys():
	print(key)

print("\nOn the following issue: " + issue)
if yes > no:
	print("Yes wins! " + str(yes) + " votes to " + str(no) + ".")
elif no > yes:
	print("No wins! " + str(no) + " votes to " + str(yes) + ".")
else:
	print("It was a tie! " + str(no) + " votes to " + str(yes) + ".")

guess = input("\nTo see the voting results enter the admin password: ")
if guess == password:
	for key, value in results.items():
		print("Voter: " + key + "\t\t\tVote: " + value)
else:
	print("Sorry, that is not the correct password.	Goodbye...")

print("\nThank you for using the Yes or No Issue Polling App.")