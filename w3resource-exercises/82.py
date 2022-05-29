###
# 82. Write a Python program to calculate the sum of all items 
# of a container (tuple, list, set, dictionary).
###

def sum_all_items(container) -> int:
    sum:int = 0

    if type(container) == dict:
        for k in container.keys():
            sum += container[k]

    else: 
        for item in container:
            sum += item


    return sum

def main():
    container_one:list = [1, 2, 3]
    container_two:tuple = (4, 5, 6)
    container_three:set = set([7, 8, 9])
    container_four:dict = {1:0, 2:1, 3:2}

    container_one_sum_all_values = sum_all_items(container_one)
    container_two_sum_all_values = sum_all_items(container_two)
    container_three_sum_all_values = sum_all_items(container_three)
    container_four_sum_all_values = sum_all_items(container_four)

    print("Sum of container: " + str(container_one_sum_all_values))
    print("Sum of container: " + str(container_two_sum_all_values))
    print("Sum of container: " + str(container_three_sum_all_values))
    print("Sum of container: " + str(container_four_sum_all_values))

if __name__ == "__main__":
    main()