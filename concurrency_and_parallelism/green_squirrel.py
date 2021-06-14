import time
from gevent.pool import Pool
from gevent import monkey

from websites import WEBSITE_LIST
from utils import check_website

# Note that you can spawn many workers with gevent since the cost
# of creating and switching is very low
NUM_WORKERS = 4

# Monkey-Patch socket module for HTTP requests
monkey.patch_socket()

start_time = time.time()

pool = Pool(NUM_WORKERS)
for address in WEBSITE_LIST:
    pool.spawn(check_website, address)

# Wait for stuff to finish
pool.join()

end_time = time.time()

print(f'Time for GreenSquirrel: {end_time - start_time}secs')