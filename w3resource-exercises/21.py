"""
21. Write a Python program to find whether a given number 
    (accept from the user) is even or odd, print out an appropriate message to the user.
"""

# Tip 1: An even number is a number that can be divided into two equal groups. 
# An odd number is a number that cannot be divided into two equal groups. 

# Tip 2: The % symbol in Python is called the Modulo Operator. 
# It returns the remainder of dividing the left hand operand by right hand operand. 
# It's used to get the remainder of a division problem.

def check_if_is_odd_or_even(number: float):
    mod = number % 2

    print(f"Remaider equals = {str(mod)}")

    if mod == 0:
        print(f"The number: {number} is even!")
    else:
        print(f"The number: {number} is odd...")


user_input = float(input("Type a number: "))

check_if_is_odd_or_even(user_input)