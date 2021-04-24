"""
45. Write a python program to call an external command in Python
"""
import os 
from subprocess import call 

pwd = os.getcwd()
file = "45.py"
full_path = os.path.join(pwd, file)

if __name__ == '__main__':
    #print(full_path)
    call(['ls', '-lrth', full_path])