"""
35. Write a Python program that will 
    return true 
        if the two given integer values are equal 
        or their sum or difference is 5
"""


def check_diff(x, y):

    if x == y:
        return True
    elif (abs(x - y) == 5) or (abs(x + y) == 5):
        return True 
    else: 
        return False 

if __name__ == '__main__':
    test_one = check_diff(10, 5)
    test_two = check_diff(5, 10)
    test_three = check_diff(25, 65)

    print(test_one)
    print(test_two)
    print(test_three)