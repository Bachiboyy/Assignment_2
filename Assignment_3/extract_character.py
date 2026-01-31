def extract_character(string):
    lenght = len(string)

    if lenght % 2 == 1:
        middle_index = lenght // 2
        return string[middle_index]
    
    if lenght % 2 == 0:
        middle_index1 = (lenght // 2) - 1
        middle_index2 = lenght // 2
        return string[middle_index1] + string[middle_index2]
    

while True:
    i = input("Enter your choice (0: Exit, 1: Extract Character): ")

    if i == '1':
        text = input("Enter a string: ")
        result = extract_character(text)
        print("The extracted character(s):", result)

    elif i == '0':
        print("Exiting the program.")
        break