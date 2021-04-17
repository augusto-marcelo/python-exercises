"""
33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""

def sum_three_numbers(n1, n2, n3):

    numbers_non_duplicated = set([n1, n2, n3])

    if len(numbers_non_duplicated) == 2:
        return 0
    else:
        return n1 + n2 + n3

    #return numbers_non_duplicated

def sum_answer(x, y, z):
    if x == y or y == z or x == z:
        return 0
    else:
        return x + y + z

if __name__ == '__main__':
    distinct = sum_three_numbers(1,2,3)
    duplicate = sum_three_numbers(1, 2, 2)

    test1 = sum_answer(1, 2, 3)
    test2 = sum_answer(1, 2, 2)
    
    print(distinct)
    print(duplicate)

    print(test1)
    print(test2)