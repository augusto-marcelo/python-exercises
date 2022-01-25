###
# 70. Write a Python program to sort files by date.
###

import glob
import os 

def main():
    files = glob.glob("*.py")
    
    #files.sort()
    files.sort(key=os.path.getmtime)

    print(files)

if __name__ == "__main__":
    main()