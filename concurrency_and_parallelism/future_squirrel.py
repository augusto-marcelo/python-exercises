"""
concurrent.futures
As stated previously, concurrent.futures is a high-level API for using threads. 
The approach we're taking here implies using a ThreadPoolExecutor. 
We're going to submit tasks to the pool and get back futures, which are results that 
will be available to us in the future. Of course, we can wait for all futures to become actual results.
"""

import time
import concurrent.futures

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    futures = {executor.submit(check_website, address) for address in WEBSITE_LIST}
    concurrent.futures.wait(futures)

end_time = time.time()

print(f"Time for FutureSquirrel: {end_time - start_time}secs")