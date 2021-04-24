"""
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, 
    and a number of years. Go to the editor
    
    Test Data : amt = 10000, int = 3.5, years = 7
    Expected Output : 12722.79
"""

def compute_future_amnt(amnt: float, rate: float, years: float):
    #return amnt * (rate / 100.0) * years
    return amnt * (1 + (rate / 100.0)) ** years

if __name__ == '__main__':
    result = compute_future_amnt(amnt=10000.0, rate=3.5, years=7)
    print(f'{result:.2f}')
