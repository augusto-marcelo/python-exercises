"""
61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""

def main():
    distance_in_feet = 100

    distance_in_inches = convert_to_inches(distance_in_feet)
    distance_in_yards = convert_to_yards(distance_in_feet)
    distance_in_miles = convert_to_miles(distance_in_feet)

    print(f"The distance in feet: {distance_in_feet}")
    print(f"The distance in inches is: {distance_in_inches:.2f} inches.")
    print(f"The distance in yards is: {distance_in_yards:.2f} yards.")
    print(f"The distance in miles is: {distance_in_miles:.2f} miles.")



def convert_to_inches(feet):
    return feet * 12

def convert_to_yards(feet):
    return feet / 3.0

def convert_to_miles(feet):
    return feet / 5280.0

if __name__ == "__main__":
    main()