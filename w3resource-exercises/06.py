"""
6. Write a Python program which accepts a sequence of comma-separated numbers
 from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

user_input = input("Type a couple of numbers separated by comma: ")

print(list(user_input.replace(",","")))
print(tuple(user_input.replace(",", "")))