"""
Threading Approach
We're going to get a bit more creative with the implementation of the threaded approach. 
We're using a queue to put the addresses in and create worker threads to get them out of the queue 
and process them. We're going to wait for the queue to be empty, meaning that all the addresses have 
been processed by our worker threads.
"""

import time
from queue import Queue
from threading import Thread

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 16
task_queue = Queue()

def worker():
    # Constantly check the queue for addresses
    #while True:
    while len(task_queue.queue) > 0:
        address = task_queue.get()
        check_website(address)

        # Mark the processed task as done
        task_queue.task_done()

start_time = time.time()

# Create the worker threads 
threads = [Thread(target=worker) for _ in range(NUM_WORKERS)]

# Add the websites to the task queue 
[task_queue.put(item) for item in WEBSITE_LIST]

# Start all the workers
[thread.start() for thread in threads]

# Wait for all the tasks in the queue to be processed
task_queue.join()

end_time = time.time()

print(f"Time for ThreadedSquirrel: {end_time - start_time}secs")
#input()
