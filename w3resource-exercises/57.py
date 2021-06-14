"""
57. Write a Python program to get execution time for a Python method.
"""
import time


def get_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time needed: {(end - start):.2} seconds")
        
    return wrapper

@get_execution_time
def count(start, stop):

    print(f"Couting from {start} to {stop}")
    for i in range(start, stop):
        pass

if __name__ == '__main__':
    count(1, 500000000)