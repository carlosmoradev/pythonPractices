correct_password = "python123"
name = input("Enter your name: ")
surname = input("Enter your surname: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password!  Please try again: ")

#print("Logged in")
message = "Hello %s %s, you are logged!" % (name, surname)
print(message)
