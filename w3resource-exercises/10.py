"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
"""

user_input_int = input("Type an integer: ")

#result = (user_input_int + user_input_int ** 2) + (user_input_int ** 3)
n1 = user_input_int
n2 = user_input_int * 2
n3 = user_input_int * 3

print(f"Result = {int(n1) + int(n2) + int(n3)}")