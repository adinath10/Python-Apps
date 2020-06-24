#Python Challenge 22	Database Admin Program

print("Welcome to the Database Admin Program")

users_login_info = {
		"mooman74" : "alskes145",
		"meramo1986" : "kehns010101",
		"nickyD" : "world1star",
		"george2" : "booo3oha",
		"admin00" : "admin1234"
		}

username = input("\nEnter your username: ")
if username in users_login_info:
	password = input("Enter your password: ")
	if password == users_login_info[username]:
		print("\nHello " + username + "!  You are logged in!")
		if username == 'admin00':
			print("\nHere is the current user database:")
			for key,value in users_login_info.items():
				print("Username: " + key + "\t\t" + "Password: " + value)
		else:
			change_pass = input("Would you like to change your password (yes/no): ").lower().strip()
			if change_pass == 'yes':
				new_pass = input("What would you like your new password to be (min 8 chars): ")
				if len(new_pass) < 8:
					print(username + " not the minimum eight characters.")
					print("\n" + username + " your password is " + password)
				else:
					users_login_info['username'] = new_pass
					print("\n" + username + " your password is " + users_login_info['username'])		
			else:
				print("\nThank you, goodbye.")
	else:
		print("Password incorrect!")
else:
	print("Username not in database, goodbye.")