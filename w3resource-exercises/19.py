"""
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
    If the given string already begins with "Is" then return the string unchanged.
"""

def change_string(string: str):
    if string.lower().startswith("is "):
        return string
    else: 
        new_string = "Is " + string
        return new_string

user_input = input("Type some text: ")
result = change_string(user_input)
print(result)