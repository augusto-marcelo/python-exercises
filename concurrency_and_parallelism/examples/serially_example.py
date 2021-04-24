"""
Here's what we're going to do: we will run, multiple times, a task outside the GIL and one inside it.
 We're running them serially, using threads and using processes.
 Let's define the tasks:
"""
import os 
import time 
import threading 
import multiprocessing

NUM_WORKERS = 4

def only_sleep():
    """ Do nothing, wait for a timer to expire """
    print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")
    time.sleep(0.5)

def crunch_numbers():
    """ Do some computations """
    print(f"PID: {os.getpid()}, Process Name: {multiprocessing.current_process().name}, Thread Name: {threading.current_thread().name}")
    x = 0
    while x < 10000000:
        x += 1


# Run tasks serially
start_time = time.time()
for _ in range(NUM_WORKERS):
    only_sleep()
end_time = time.time()

print(f"Serial time = {end_time - start_time}")

# Run tasks using threads 
start_time = time.time()
threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WORKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time = time.time()

print(f"Threads time={end_time - start_time}")

# Run tasks using processes 
start_time = time.time()
processes = [multiprocessing.Process(target=only_sleep()) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()

print(f"Parallel time={end_time - start_time}")


"""
Let's do the same routine but this time running the crunch_numbers task:
"""
print('\n\n....Starting comparission for crunch_numbers task....\n\n\n')

start_time = time.time()
for _ in range(NUM_WORKERS):
    crunch_numbers()
end_time = time.time()

print(f"Serial time={end_time - start_time}")

start_time = time.time()
threads = [threading.Thread(target=crunch_numbers) for _ in range(NUM_WORKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time = time.time()

print(f"Threads time= {end_time - start_time}")

start_time = time.time()
processes = [multiprocessing.Process(target=crunch_numbers) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()

print(f"Parallel time= {end_time - start_time}")