"""
47. Write a Python program to find out the number of CPUs using. 
"""
import multiprocessing


if __name__ == '__main__':
    print(f'CPU count = {multiprocessing.cpu_count()}')