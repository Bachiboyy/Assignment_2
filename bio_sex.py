bio_sex = input("Please enter your biological sex (M for male, F for female) ")
hemo_values = int(input("Please enter your hemoglobin values (g/l): "))
if bio_sex.lower() == "m":
    print("You are identified as male.")
    if hemo_values < 134:
        print("Your hemoglobin values are low.")
    elif 134 <= hemo_values <= 170:
        print("Your hemoglobin values are normal.")
    else:
        print("Your hemoglobin values are high.")
elif bio_sex.lower() == "f":
    print("You are identified as female.")
    if hemo_values < 117:
        print("Your hemoglobin values are low.")
    elif 117 <= hemo_values <= 155:
        print("Your hemoglobin values are normal.")
    else:
        print("Your hemoglobin values are high.")
else:
    print("Invalid input for biological sex. Please enter 'M' for male or 'F' for female.")