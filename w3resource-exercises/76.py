###
# 76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) 
# passed to a script.
###
import sys

def main():
    script_name = sys.argv[0]
    qtty_of_args = len(sys.argv) - 1

    print(f"Script name: {script_name}")
    print(f"Qtty of args: {qtty_of_args}")
    
    if len(sys.argv) > 1:
        print("\nArgs: ")
        for i in range(1, len(sys.argv)):
            print(f"\t {i -1}: {sys.argv[i]}")


if __name__ == "__main__":
    main()