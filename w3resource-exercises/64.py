####
# 64. Write a Python program to get file creation and modification date/times
###

import os.path
import time

def get_file_metadata(fname):
    last_mod_time = time.ctime(os.path.getmtime(fname))
    ctime = time.ctime(os.path.getctime(fname))

    return { "last_mod_time": last_mod_time, "ctime": ctime }

def main():
    fname = input("File name please: ")
    result = get_file_metadata(fname)
    print(result)


if __name__ == "__main__":
    main()
