###
# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, 
# a millimeter of mercury (mmHg) and atmosphere pressure.
###

def convert_pressure(klp: float) -> dict:
    
    pounds_per_sq_inch = klp / 6.89475729
    mmhg = klp * 760 / 101.325
    atmosphere = klp / 101.325

    result = dict()

    result["pounds_per_sq_inch"] = pounds_per_sq_inch
    result["mmhg"] = mmhg
    result["atmosphere"] = atmosphere

    return result


def main():
    klp = 12.35 
    result = convert_pressure(klp)

    print(result)

if __name__ == "__main__":
    main()