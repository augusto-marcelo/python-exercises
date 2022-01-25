###
# 68. Write a Python program to calculate the sum of the digits in an integer
###


def calc(num: str) -> int:
    
    total: int = 0
    
    for i in str(num):
        total += int(i)

    return total



def main():
    num = "5245"
    result = calc(num)

    print(result)

if __name__ == "__main__":
    main()