"""
36. Write a Python program to add two objects if both objects are an integer type.
"""

def add_only_int(x, y):
    if type(x) == int and type(y) == int:
        return x + y
    else:
        return None



#exercise answer
def add_number(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError('Inputs must be Integers')
    
    return a + b

if __name__ == '__main__':
    test_one = add_only_int(2, 4)
    test_two = add_only_int(1, 'asfd')

    print(test_one)
    print(test_two)

    print("...")

    test_three = add_number(10, 20)
    print(test_three)
    
    test_four = add_number(1, 'asdf')
    print(test_four)