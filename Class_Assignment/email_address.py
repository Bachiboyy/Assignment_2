def count_a(email):
    count = 0
    for char in email.lower():
        if char == "@":
            count += 1
    return count


def extract_username(email):
    if count_a(email) != 1:
        return None, None

    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index + 1:]
    return username, domain


while True:
    i = input("Enter your choice (0: Exit, 1: Extract Username and Domain): ")

    if i == '1':
        email = input("Enter an email address: ")
        username, domain = extract_username(email)

        if username is None:
            print("Invalid email address")
        else:
            print("User", username, "is logged in from", domain)

    elif i == '0':
        print("Exiting the program.")
        break