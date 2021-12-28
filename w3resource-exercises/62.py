####
# 62. Write a Python program to convert all units of time into seconds.
###

HOUR_IN_SEC=3600
MIN_IN_SEC=60

def convert(hour: int, minute: int, sec: int):
    result = 0
    
    result += hour * HOUR_IN_SEC
    result += minute * MIN_IN_SEC
    result += sec

    return result


def main():
    hour = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    secs = int(input("Seconds: "))

    result = convert(hour, minutes, secs)

    print("Result: " + str(result))


if __name__ == '__main__':
    main()