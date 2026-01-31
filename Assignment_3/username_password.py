username = "python"
password = "rules"

count = 0

while True:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    if input_username == username and input_password == password:
        print("Wekcome")
        break
    else:
        print("Invalid username or password. Please try again.")
        count += 1

    if count == 5:
        print("Access denied.")
        break