import math

def enter_pizza_details():
    diameter = float(input("Enter the diameter of the pizza (in cm): "))
    price = float(input("Enter the price of the pizza (in $USD): "))
    return diameter, price

def price_per_meter(diameter, price):
    radius = diameter / 2
    radius_meters = radius / 100
    area = math.pi * (radius_meters ** 2)
    return price / area

print("Enter details for Pizza 1:")
diameter1, price1 = enter_pizza_details()
pizza1 = price_per_meter(diameter1, price1)
print("Enter details for Pizza 2:")
diameter2, price2 = enter_pizza_details()
pizza2 = price_per_meter(diameter2, price2)

print("Price per square meter for Pizza 1:", f"{pizza1:.2f}")
print("Price per square meter for Pizza 2:", f"{pizza2:.2f}")

if pizza1 < pizza2:
    print("Pizza 1 is the better deal.")
elif pizza2 < pizza1:
    print("Pizza 2 is the better deal.")