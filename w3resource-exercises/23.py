"""
23. Write a Python program to get the n (non-negative integer) copies of the first 2 
    characters of a given string. Return the n copies of the whole string if the length is less than 2. 
"""



def get_copies(some_string: str, number_of_copies: int):

    if len(some_string) < 2:
        return some_string * number_of_copies
    else:
        first_two_chars = some_string[:2]
        return first_two_chars * number_of_copies

if __name__ == '__main__':
    print(get_copies('abcdef', 2))
    print(get_copies('p', 3))

