cabin_class = input("Please enter your cabin class (LUX, A, B, C): ")
if cabin_class.lower() == "lux":
    print("Your class is LUX. Upper-deck cabin with a balcony.")
elif cabin_class.lower() == "a":
    print("Your class is A. Above the car deck, equipped with a window.")
elif cabin_class.lower() == "b":
    print("Your class is B. Windowless cabin above the car deck.")
elif cabin_class.lower() == "c":
    print("Your class is C. Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")