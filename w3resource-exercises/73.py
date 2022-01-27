####
# 73. Write a Python program to calculate midpoints of a line
####

def get_line_mid_points(x1, y1, x2, y2) -> float:
    
    x_mid_point = (x1 + x2) / 2

    y_mid_point = (y1 + y2) / 2
    
    return x_mid_point, y_mid_point


def main():
    x1, y1, x2, y2 = (2, 2, 4, 4)
    line_mid_point = get_line_mid_points(x1, y1, x2, y2)

    print(f"Line length {x1, y1, x2, y2}")
    print(f"Line midpoint: {line_mid_point}")

if __name__ == "__main__":
    main()