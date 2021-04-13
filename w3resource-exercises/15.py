"""
15. Write a Python program to get the volume of a sphere with radius 6.

The formula for the volume of a sphere is V = 4/3 πr³.
"""
from math import pi

def get_sphere_volume(radius: float):
    volume = 4.0 / 3.0 * pi * radius ** 3
    return volume

radius_input = float(input("Type the radius: "))

sphere_volume = get_sphere_volume(radius_input)

print(f"The Volume of a Sphere with radius = {radius_input} is {sphere_volume:2.8f} m3")
