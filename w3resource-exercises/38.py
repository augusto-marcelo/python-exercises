"""
38. Write a Python program to solve (x + y) * (x + y). Go to the editor
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""


def sum_and_pow(x, y):
    return (x + y) ** 2

if __name__ == '__main__':
    print(sum_and_pow(4, 3))