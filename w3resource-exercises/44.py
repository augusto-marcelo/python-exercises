"""
44. Write a Python program to locate Python site-packages.
"""
import site

if __name__ == '__main__':

    for path in site.getsitepackages():
        print(path)
    