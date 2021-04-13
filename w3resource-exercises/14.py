"""
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

import datetime

newest_date = (2014, 7, 11)
oldest_date = (2014, 7, 2)

diff = datetime.date(oldest_date) - datetime.date(newest_date)
print(f"{str(diff.days)} days")