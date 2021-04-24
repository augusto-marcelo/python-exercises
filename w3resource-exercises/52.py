"""
52. Write a Python program to print to stderr. 
"""

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")

"""
when ran by the terminal don't forget to use: python 52.py 2> 52.txt (e.g 2> redirects the error to wherever you want)
"""