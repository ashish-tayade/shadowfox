# 04_conditions.py
# BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")

# City to Country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter city: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")

# Two city check
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

if (city1 in India and city2 in India):
    print("Both cities are in India")
elif (city1 in UAE and city2 in UAE):
    print("Both cities are in UAE")
elif (city1 in Australia and city2 in Australia):
    print("Both cities are in Australia")
else:
    print("They don't belong to same country")