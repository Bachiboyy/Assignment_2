while True:
    value = float(input("Enter value in inches: "))
    if value < 0:
        print("Exiting the program. The value is negative.")
        break
    value_cm = value * 2.54
    print(value, "inches is", value_cm, "cm")