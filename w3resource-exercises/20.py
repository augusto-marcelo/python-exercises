"""
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. 
"""

def multiply_string(text: str, n: int):
    return text * abs(n)

text = input("Type a text to be multiplied: ")
n = int(input("Now, the number of times it should be multiplied: "))

result = multiply_string(text, n)
print(result)