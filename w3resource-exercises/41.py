"""
41. Write a Python program to check whether a file exists.
"""
import os

pwd = os.getcwd()
user_login = os.getlogin()
pid = os.getpid()

file_name = '41.py'
path = os.path.join(pwd, file_name)
file_exists = os.path.isfile(path)

if __name__ == '__main__':
    print(pwd)
    print(user_login)
    print(pid)
    print(path)
    print(file_exists)
    print()