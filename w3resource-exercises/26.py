"""
26. Write a Python program to create a histogram from a given list of integers.
"""

#MY SOLUTION
'''
def build_histogram(data_array: list):
    print_char = "@"

    for qtty in data_array: 
        print(print_char * qtty)



if __name__ == '__main__':
    build_histogram([2, 3, 6, 5])
'''

# SOLUTION FROM THE WEBSITE
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])