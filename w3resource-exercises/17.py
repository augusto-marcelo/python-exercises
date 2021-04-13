"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000
"""


def test_number(n: float):
    if n >= 100 and n < 1000:
        print("Number is between 100 & 1000")
    elif n >= 1000 and n < 2000:
        print("Number is between 1000 & 2000")
    elif n >= 2000:
        print("Number is greater than 2000")

user_input = float(input("Type a number: "))
test_number(user_input)