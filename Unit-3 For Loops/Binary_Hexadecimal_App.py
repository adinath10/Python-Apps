#Python Challenge 11	Binary/Hexadecimal Converter App

print("Welcome to the Binary/Hexadecimal Converter App")

max_value = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_value+1))
binary  = []
hexadecimal = []
for num in decimal:
	binary.append(bin(num))
	hexadecimal.append(hex(num))
print("Generating lists....complete!")

print("\nUsing slices, we will now show a portion of each list.")
lower_range = int(input("What decimal number would you like to Start at: "))
upper_range = int(input("What decimal number would you like to Stop at: "))

print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) + " :")
for num in decimal[lower_range-1:upper_range]:
	print(num) 

print("\nBinary values from " + str(lower_range) + " to " + str(upper_range) + " :")
for num in binary[lower_range-1:upper_range]:
	print(num)

print("\nDecimal values from " + str(lower_range) + " to " + str(upper_range) + " :")
for num in hexadecimal[lower_range-1:upper_range]:
	print(num)

input("Press Enter to see all values from 1 to " + str(max_value) + ".")
print("Decimal----Binary----Hexadecimal")
print("------------------------------------------------------------------------------")
for d,b,h in zip(decimal, binary, hexadecimal):
	print(str(d) + "----" + str(b) + "----" + str(h))