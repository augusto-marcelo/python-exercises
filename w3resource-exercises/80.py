###
# 80. Write a Python program to get the current value of the recursion limit.
###
import sys

def main():
    rec_limit = sys.getrecursionlimit()
    print(f"Current value of the recursion limit: {rec_limit}") 

if __name__ == "__main__":
    main()