###
# 72. Write a Python program to get the details of math module.
###
import math
import inspect

def main():
    print(type(math))
    print("#" * 10)

    print(dir(math))
    print("#" * 10)

    print(inspect.getmembers(math))
    print("#" * 10)
    
if __name__ == "__main__":
    main()