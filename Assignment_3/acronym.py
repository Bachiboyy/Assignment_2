def generate_acronym(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        if word:  # Ensure the word is not empty
            acronym += word[0].upper()
    return acronym

while True:
    phrase = input("Enter a phrase (or type 'exit' to quit): ")
    if phrase.lower() == 'exit':
        print("Exiting the program.")
        break
    acronym = generate_acronym(phrase)
    print("The acronym is:", acronym)