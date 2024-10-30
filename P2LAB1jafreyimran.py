
 # Imran Hassan Jafrey
# 2024-10-07
# Assignment Name: Circle Calculations
# This program takes the radius of a circle from the user and calculates the diameter, circumference, and area of the circle.
# It then displays the results with specific formatting:
# Diameter has one decimal place, circumference has two, and area has three.

import math

# Taking the radius as input from the user
radius = float(input("What is the radius of the circle? "))

# Calculating diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Displaying the results with the required formatting
print(f"\nThe diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
