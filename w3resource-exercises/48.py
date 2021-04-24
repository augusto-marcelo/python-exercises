"""
48. Write a Python program to parse a string to Float or Integer. Go to the editor
"""

user_input = input("Insert an Integer or a Float: ")
try:
    print("Trying to convert to int")
    to_int = int(user_input)
    print(to_int)
except ValueError as v: 
    print("You've provided a float")
    to_float = float(user_input)
    print(to_float)