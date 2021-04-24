"""
49. Write a Python program to list all files in a directory in Python.
"""

import os
import glob

pwd = os.getcwd()

#print(glob.glob(pwd + "/*"))

for file in glob.glob(pwd + "/*"):
    print(file)