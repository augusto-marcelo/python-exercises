"""
46. Write a python program to get the path and name of the file that is currently executing. 
"""
import os

if __name__ == '__main__':
    print(os.path.realpath(__file__))