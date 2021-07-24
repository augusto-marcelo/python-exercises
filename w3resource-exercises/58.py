"""
58. Write a Python program to sum of the first n positive integers.
"""

def main():
    numbers = [1, 2, 3, 5, 6, 7, 8, 9]

    print(sum(0, numbers))
    print(sum(1, numbers))
    print(sum(2, numbers))
    print(sum(5, numbers))

def sum(n, numbers_list):

    temp = 0

    for i in range(n):
        temp += numbers_list[i]

    return temp


if __name__ == '__main__':
    print("running")
    main()