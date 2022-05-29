###
# 79. Write a Python program to get the size of an object in bytes
###
import sys

def main():

    objects = ["one", "four", "three", 0, 112, 122.56]

    for obj in objects:
        size_in_bytes = sys.getsizeof(obj)
        print(f"Size of {obj} in bytes = {size_in_bytes}")

    pass 

if __name__ == "__main__":
    main()