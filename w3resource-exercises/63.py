####
# 63. Write a Python program to get an absolute file path.
###

import os.path

def get_absolute_path(path):
    return os.path.abspath(path)

def main():

    fname = input("File: ")
    abs_path = get_absolute_path(fname)
    print(abs_path)


if __name__ == '__main__':
    main()