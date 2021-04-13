"""
22. Write a Python program to count the number 4 in a given list
"""

def count_number_four(array: list):

    counter = 0
    for item in array:
        if item == 4:
            counter += 1

    return counter

if __name__ == "__main__":
    sample_list = [2, 3, 4, 5, 6, 5, 4, 6, 7, 5, 4]
    total = count_number_four(sample_list)
    print(f"The counter is: {total}")