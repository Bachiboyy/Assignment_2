
def count_wovels(s):
    vowels = "euoai"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1
    return count

while True:
    i = input("Enter your choice (0: Exit, 1: Count Vowels): ")
    if i == '1':
        text = input("Enter a string: ")
        result = count_wovels(text)
        print("The number of vowels in the string is:", result)
    elif i == '0':
        print("Exiting the program.")
        break