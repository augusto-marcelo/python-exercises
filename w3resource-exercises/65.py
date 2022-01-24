###
# 65. Write a Python program to convert seconds to day, hour, minutes and seconds. Go to the editor
###

import math



def convert(seconds: int) -> dict:

    ONE_MINUTE_IN_SECONDS = 60
    ONE_HOUR_IN_SECONDS = ONE_MINUTE_IN_SECONDS * 60
    ONE_DAY_IN_SECONDS = ONE_HOUR_IN_SECONDS * 24    
    
    sec_to_days = seconds // ONE_DAY_IN_SECONDS
    seconds %= ONE_DAY_IN_SECONDS

    sec_to_hours = seconds // ONE_HOUR_IN_SECONDS
    seconds %= ONE_HOUR_IN_SECONDS

    sec_to_mins = seconds // ONE_MINUTE_IN_SECONDS
    seconds %= ONE_MINUTE_IN_SECONDS
    
    result = dict()

    result["days"] = sec_to_days
    result["hours"] = sec_to_hours
    result["minutes"] = sec_to_mins
    result["seconds"] = seconds

    return result


def main() -> int:
    seconds_to_convert = 1234565

    convertion_result = convert(seconds_to_convert)

    print(convertion_result)

if __name__ == "__main__":
    main()