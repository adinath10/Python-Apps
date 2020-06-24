#Python Challenge 21	Thesaurus App

import random

print("Welcome to the Thesaurus App!")

print("\nChoose a word from the thesaurus and I will give you a synonym.")

synonyms = {
	'Hot' : ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
	'Cold' : ['chilly', 'cool','freezing','frigid','polar'],
	'Happy' : ['content', 'cheery', 'merry', 'jovial', 'jocular'],
	'Sad' :  ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
	}

print("\nHere are the words in the thesaurus:")
for keys in synonyms.keys():
	print("\t-" + keys.lower())
	 
syn = input("\nWhat word would you like a synonym for: ").title().strip()

if syn in synonyms.keys():
	print("A synonym for " + syn.lower() + " is " + random.choice(synonyms[syn]) + ".")

	choice = input("\nWould you like to see the whole thesaurus (yes/no): ").lower().strip()
	if choice == 'yes':
		for keys,values in synonyms.items():
			print("\n" + keys + " synonyms are: ")
			for value in values:
				print("\t- ", value)
	else:
		print("\nI hope you enjoyed the program.	Thank you!")

else:
	print("I'm sorry, that word is not currently in the thesaurus.")

