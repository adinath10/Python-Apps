#Python Challenge 16	Shipping Accounts Program

print("Welcome to the Shipping Accounts Program")

users = ['N', 'My', 'Forever', 'L', 'Adinath']

username = input("\nHello, what is your username: ").lower().strip()

if username in users:
	print("\nHello " + username + ".  Welcome back to account.")
	print("Current shipping prices are as follows:")
	print("\nShipping orders 0 to 100:		$5.10 each")
	print("Shipping orders 101 to 500:		$5.00 each")
	print("Shipping orders 501 to 1000:		$4.95 each")
	print("Shipping orders over 1000:		$4.80 each")

	items = int(input("\nHow many items would you like to ship: "))
	if items <= 100:
		item = items * 5.10
		item = round(item, 2)
		print("To ship " + str(items) + " items it will cost you $" + str(item) + " at $5.10 per item.")
	elif items <= 500:
		item = items * 5.00
		item = round(item, 2)
		print("To ship " + str(items) + " items it will cost you $" + str(item) + " at $5.00 per item.")
	elif items <= 1000:
		item = items * 4.95
		item = round(item, 2)
		print("To ship " + str(items) + " items it will cost you $" + str(item) + " at $4.95 per item.")
	else:
		item = items * 4.80
		item = round(item, 2)
		print("To ship " + str(items) + " items it will cost you $" + str(item) + " at $4.80 per item.")

	confirm = input("\nWould you like to place this order(y/n): ").lower().strip()
	if confirm == 'y':
		print("Okay, Shipping your " + str(items) + " items.")
	elif confirm == 'n':
		print("Okay, no order is being placed at this time.")
else:
	print("Sorry, you do not have an account with us.	Goodbye.")

