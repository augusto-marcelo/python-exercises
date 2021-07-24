"""
60. Write a Python program to calculate the hypotenuse of a right angled triangle
"""
from math import sqrt

def main():
    a = 3
    b = 4

    c = find_length(a, b)

    print(f"The length of the hypotenuse is: {c}")

def find_length(a, b):
    return sqrt(a**2 + b**2)



if __name__ == "__main__":
    main()