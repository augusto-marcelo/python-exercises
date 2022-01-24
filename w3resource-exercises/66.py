###
# 66. Write a Python program to calculate body mass index. 
### 
import math

def calc_mass(weight: float, height: float) -> float:

    # BMI = kg/m² where kg is a person's weight and m² is their height in metres squared.
    
    body_mass_index = weight / height ** 2

    return body_mass_index


def main():
    weight = 65
    height = 6

    bmi = calc_mass(weight, height)

    print(round(bmi, 2))


if __name__ == "__main__":

    main()