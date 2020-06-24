#Python Challenge 18	Voter Registration App

print("Welcome to the Voter Registration App")

name = input("\nPlease enter your name: ").title().strip()
age = int(input("Please enter your age: "))

if age <= 17:
	print("\nYou are not old enough to register to vote")
else:
	print("\nCongratulations " + name + "! You are old enough to register to vote.")
	
	parties = ['Republican','Democratic','Independent','Libertarian','Green']

	print("\nHere is list of political parties to join.")
	for party in parties:
		print("\t -", party) 
	
	party_name = input("\nWhat party would you like to join: ").title().strip()
	
	if party_name in parties:
		print("\nCongratulations " + name + "! You have joined the " + party_name + " party!")
		if party_name == 'Republican' or party_name == 'Democratic':
			print("That is a major party!")	
		elif party_name == 'Independent':
			print("You are an Independent party!")
		else:
			print("That is a not major party!")
	else:
		print("That is not given party!")