arr = []

def find_max(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max

def find_min(arr):
    min = arr[0]
    for num in arr:
        if num < min:
            min = num
    return min  

count = 0

while True:
    value = input("Enter a number:")
    if value == "":
        print("Exiting the program. The input is an empty string.")
        break
    arr.append(float(value))
    count += 1

max_value = find_max(arr)
min_value = find_min(arr)
print("Total numbers entered:", count)
print("The maximum value is:", max_value)
print("The minimum value is:", min_value)