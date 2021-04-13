"""
27. Write a Python program to concatenate all elements in a list into a string and return it. 
"""

def join_elements(list_of_elements: list) -> str: 
    
    new_string: str = ''

    for item in list_of_elements:
        new_string += str(item)

    return new_string


if __name__ == '__main__':
    list_of_elements = ['a', 1, True]

    print(join_elements(list_of_elements))