length = int(input("Enter the length of the zander in cm: "))
min = 42
if length < min:
    print("The zander is too small to keep.")
    print("Minimum length is", min, "cm.")
    length_to_grow = min - length
    print("The zander is ", length_to_grow, "cm less than legal size.")
else:
    print("The zander is of legal size to keep.")
    print("Congratulations!")