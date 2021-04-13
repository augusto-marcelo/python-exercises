"""
25. Write a Python program to check whether a specified value is contained 
    in a group of values. Go to the editor

    Test Data :
    3  ->  [1, 5, 8, 3] : True
    -1 -> [1, 5, 8, 3] : False
"""

def test_existence(group_of_values: list, value: int) -> bool:

    for item in group_of_values:
        if value == item:
            return True

    return False


if __name__ == '__main__':
    group_one = [1, 5, 8, 3]
    group_two = [1, 5, 8, 3]

    test_one = test_existence(group_one, 3)
    test_two = test_existence(group_two, -1)

    print(f"Test ONE = {test_one}")
    print(f"Test TWO = {test_two}")