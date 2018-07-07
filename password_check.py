correct_password = "python123"
name = input("Enter your name: ")
surname = input("Enter your surname: ")
password = input("Enter password: ")

while password != correct_password:
    password = input("Wrong password. Try again: ")

print("Hi %s %s, you are logged in!" %(name,surname))