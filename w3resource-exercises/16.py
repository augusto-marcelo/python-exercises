"""
16. Write a Python program to get the difference between a given number and 17, 
    if the number is greater than 17 return double the absolute difference.
"""



def get_absolute_different(number: float):
    if number <= 17:
        return number - 17
    else:
        return (number - 17) ** 2

number_input = float(input("Type a number: "))
result = get_absolute_different(number_input)

print(str(result))