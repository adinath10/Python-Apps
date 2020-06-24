#Python Challenge 14	Fibonacci Calculator App

print("Welcome to the Fibonacci Calculator App.")

number = int(input("\nHow many digits of the Fibonacci Sequence would you like to compute: "))

print("\nThe first " + str(number) + " numbers of the Fibonacci Sequence are: ")

fib = [1,1]

for i in range(number - 2):
	new_fib = fib[i] + fib[i + 1]
	fib.append(new_fib)

for number in fib:
	print(number)

golden = []
for i in range(len(fib)-1):
	ratio = fib[i+1]/fib[i]
	golden.append(ratio)

print("\nThe corresponding Golden Ratio values are: ")
for ratio in golden:
	print(ratio)

print("\nThe ratio of consecutive Fibonacci terms approches Phi; 1.618...")