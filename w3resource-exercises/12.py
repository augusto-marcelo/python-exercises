"""
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

import calendar

year_input = int(input("Type the year: "))
month_input = int(input("Type the month: "))

print(calendar.month(year_input, month_input))