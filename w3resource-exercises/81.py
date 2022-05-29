###
# 81. Write a Python program to concatenate N strings
###


def concatenate(*args):
    result = ""

    for txt in args:
        result += txt
        result += " "

    return result

def main():
    answer = concatenate("concat", "me!")
    print(answer)


if __name__ == "__main__":
    main()