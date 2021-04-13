"""
18. Write a Python program to calculate the sum of three given numbers, 
    if the values are equal then return three times of their sum.
"""

def is_equals(*args):
    equals_sw = True
    #In the first occourrence of a non equal value, break and return false
    for n in args:
        try:
            if n != args[n + 1]:
                equals_sw = False
                break
        except IndexError as e:
            pass
    
    return equals_sw
        

def calculate_sum(n1, n2, n3):
    same_numbers = is_equals(n1, n2, n3)
    if not same_numbers:
        return n1 + n2 + n3
    else:
        return (n1 + n2 + n3) ** 3

distinct_numbers = calculate_sum(1, 2, 3)
same_numbers = calculate_sum(2,2,2)

print(distinct_numbers)
print(same_numbers)
