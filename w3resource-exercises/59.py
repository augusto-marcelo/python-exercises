"""
59. Write a Python program to convert height (in feet and inches) to centimeters.
"""

def main():
    feet = 4
    inch = 0

    result = convert_feet_to_centimeters(feet, inch)

    print(f"Your height is: {result}cm.")


def convert_feet_to_centimeters(feet, inch):
    h_inch = inch + (feet * 12)
    h_cm = round(h_inch * 2.54, 1)

    return h_cm



if __name__ == '__main__':
    main()