"""
Serial Approach
"""

import time 

from utils import check_website
from websites import WEBSITE_LIST

start_time = time.time()

for address in WEBSITE_LIST:
    check_website(address)

end_time = time.time()

print(f"Time for SerialSquirrel: {end_time - start_time}secs")
