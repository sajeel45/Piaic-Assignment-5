# - Calculate your age based on the current year and your birth year.

currentYear:int = 2024
birthYear:int = 2001
myage:int = currentYear - birthYear

print("My Age: ", myage)


#  - Write a program that calculates the area of a rectangle using length and width variables.

length:int = 10
width:int = 4

area:int = length * width

print("Area of Rectangle: ",area)

#  - Write a program that calculates the area of a circle.

pi:float = 3.14

radius:int = 2

areaOfCircle =  pi * radius**2

print("Area of Circle: ",areaOfCircle)

#  - Write a program that calculates the area of the cube. formula = 6a**2

surfaceArea = 4

areaOfCube = 6 * surfaceArea**2

print("Area of Cube: ",areaOfCube)

#  - Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.

temparature:int = 100

celsius:float = (temparature - 32) * 5 / 9

farenheit:float = (temparature * 9 / 5) + 32

print("Temperature in Celsius ",celsius)
print("Temperature in Farenheit ",farenheit)



#  - Convert a given number of seconds into minutes and seconds using variables.

total_seconds = 500 

minutes = total_seconds // 60  
seconds = total_seconds % 60   

result = f"{minutes} minutes and {seconds} seconds"
print(result)

#  - Write a program that calculates the percentage.

value = 40

totalValue = 100

percentageValue = value * 100 / totalValue

print("Percentage Value: ",percentageValue)

# - Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.

height_meters = 1.62  
weight_kg = 87    

bmi = weight_kg / (height_meters ** 2)

print(f"The calculated BMI is {bmi:.2f}")

# - Write a program that calculates the volume of a cylinder using the formula .

a:int = 10
volumeCube:int = a**3
print("Volume of Cube: ",volumeCube)