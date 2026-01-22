year = int(input("Please enter a year: "))
           
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
if is_leap_year(year):
    print("The year", year, "is a leap year.")
else:
    print("The year", year, "is not a leap year.")