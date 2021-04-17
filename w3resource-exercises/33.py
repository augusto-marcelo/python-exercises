"""
34. Write a Python program to sum of two given integers. 
    However, if the sum is between 15 to 20 it will return 20. 
"""

def sum_two_numbers(n1, n2):

    result = n1 + n2

    if result in range(15, 21):
        return 20
    else:
        return result

if __name__ == '__main__':
    print(sum_two_numbers(10,10))
    print(sum_two_numbers(15, 15))
