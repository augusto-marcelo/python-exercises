"""
31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
"""

# answwer from the site
def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break

    return gcd 


def optimized_gcd(x, y): 

    if x % y == 0:
        return y

    for k in range(int(y), 0 , -1):
        if x % k == 0 and y % k == 0:
            return k




print(gcd(12, 17))
print(gcd(4, 6))
print(gcd(16, 36))

print()

print(optimized_gcd(12, 17))
print(optimized_gcd(4, 6))
print(optimized_gcd(16, 36))