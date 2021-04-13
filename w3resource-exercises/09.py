"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
from datetime import datetime as dt 

exam_st_date = (11, 12, 2014)

formated_date = dt(month=exam_st_date[0], day=exam_st_date[1], year=exam_st_date[2]).strftime("%m/%d/%Y")

print(f"The examination will start from : {formated_date}")