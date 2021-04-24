"""
40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
"""
from math import sqrt

point_one = {'x': 4, 'y': 3}
point_two = {'x': 3, 'y': -2}

def calc_distance(points_one: dict, points_two: dict):

    step_one = (points_two['x'] - points_one['x']) ** 2
    step_two = (points_two['y'] - points_one['y']) ** 2

    return sqrt(step_one + step_two)

if __name__ == '__main__':
    test_one = calc_distance(point_one, point_two)
    test_two = calc_distance({'x': 4, 'y': 0}, {'x': 6, 'y': 6})
    
    print(f'{test_one:.3f}')
    print(f'{test_two}')