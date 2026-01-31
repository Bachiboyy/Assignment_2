import random
i = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess (1-10), or 0 to exit: "))
    if guess == 0:
        print("Exiting the program.")
        break
    elif guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10.")
    elif guess == i:
        print("Congratulations! You guessed the correct number:", i)
        break
    elif guess < i:
        print("Your guess is too low. Try again.")
    elif guess > i:
        print("Your guess is too high. Try again.")