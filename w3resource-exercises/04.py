"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
from math import pi

user_input = input("Type the area: ")

circle_area = pi * float(user_input) ** 2

print(f"The area is equals to = {circle_area}")