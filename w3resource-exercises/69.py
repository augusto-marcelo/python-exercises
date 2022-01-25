###
# 69. Write a Python program to sort three integers without using conditional statements and loops.
###

def sort(num_list: list) -> list:

    idx = 0
    
    while idx < len(num_list) -1: 
        if num_list[idx] > num_list[idx + 1]:
            temp = num_list[idx + 1]

            # swap
            num_list[idx + 1] = num_list[idx]
            num_list[idx] = temp

            idx = 0
        else:
            idx += 1
        


def main():
    num_list = [3, 7, 2, 4, 88, 99, 45]

    print("BEFORE: " + str(num_list))
    sort(num_list)
    print("AFTER: " + str(num_list))


if __name__ == "__main__":
    main()