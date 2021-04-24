"""
The Multiprocessing Approach
The multiprocessing library provides an almost drop-in replacement API for the threading library. 
In this case, we're going to take an approach more similar to the concurrent.futures one.
We're setting up a multiprocessing.Pool and submitting tasks to it by mapping a function to the list 
    of addresses (think of the classic Python map function).
"""
import time
import socket 
import multiprocessing

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

start_time = time.time()

with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
    results = pool.map_async(check_website, WEBSITE_LIST)
    results.wait()

end_time = time.time()

print(f"Time for MultiprocessingSquirrel: {end_time - start_time}secs")

