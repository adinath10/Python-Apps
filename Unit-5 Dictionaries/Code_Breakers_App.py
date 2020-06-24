#Python Challenge 25	Code Breakers App

from collections import Counter

print("Welcome to the Frequency Analysis App")

non_letters = ['1','2','3','4','5','6','7','8','9',' ','.','?','!',',','"',"'",':',';','(',')','%','$','&','#','\n','\t']
key_phrase_1 = """Let me till you that Never Give Up on your Dreams! and...."""
key_phrase_1 = key_phrase_1.lower()

for non_letter in non_letters:
	key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)

letter_count = Counter(key_phrase_1)
	
print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
	percentage = 100*value/total_occurrences
	percentage = round(percentage, 2)
	print("\t" + key + '\t\t' + str(value) + "\t\t" + str(percentage) + "%")

#letters from highest to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
	key_phrase_1_ordered_letters.append(pair[0])

print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_1_ordered_letters:
	print(letter, end='')

key_phrase_2 = """I said, I will not Quit the match!"""
key_phrase_2 = key_phrase_2.lower()

for non_letter in non_letters:
	key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurrences = len(key_phrase_2)

letter_count = Counter(key_phrase_2)
	
print("\n\nHere is the frequency analysis from key phrase 2: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
	percentage = 100*value/total_occurrences
	percentage = round(percentage, 2)
	print("\t" + key + '\t\t' + str(value) + "\t\t" + str(percentage) + "%")

#letters from highest to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []
for pair in ordered_letter_count:
	key_phrase_2_ordered_letters.append(pair[0])

print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_2_ordered_letters:
	print(letter, end='')

choice = input("\n\nWould you like to encode or decode a message: ").lower().strip()
phrase = input("What is the phrase: ").lower()

for non_letter in non_letters:
	phrase = phrase.replace(non_letter, '')

if choice == 'encode':
	encoded_phrase = []
	for letter in phrase:
		index = key_phrase_1_ordered_letters.index(letter)
		letter = key_phrase_2_ordered_letters[index]
		encoded_phrase.append(letter)
	
	print("\nThe encoded message is: ")
	for letter in encoded_phrase:
		print(letter, end='')
elif choice == 'decode':
	decoded_phrase = []
	for letter in phrase:
		index = key_phrase_2_ordered_letters.index(letter)
		letter = key_phrase_1_ordered_letters[index]
		decoded_phrase.append(letter)
	
	print("\nThe decoded message is: ")
	for letter in decoded_phrase:
		print(letter, end='')
else:
	print("\nPlease type encode or decode try again!!!")