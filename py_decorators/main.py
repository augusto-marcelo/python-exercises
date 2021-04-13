import time
from decorators import measure_time, sleep, startstop, debug, do_twice, repeat


def greet(name):
    return f'Hello, {name}'


def simon(func):
    return func('Simon')


@startstop
def roll():
    print("Rolling the dice")

#roll = startstop(roll)

@measure_time
def waste_time():
    print(f'Total = {str(sum([i**2 for i in range(1000000)]))}')

@sleep
def wakeup():
    print("Get up! Your break is over.")
    return "complete"

@debug
def scare():
    print("Boo!")


#@debug
#@do_twice
@repeat
def say_weeh(name):
    print(f'Weeh {name}')




if __name__ == '__main__':
    #print(simon(greet))
    #roll()
    #waste_time()
    #print(wakeup())
    #scare()
    say_weeh('Dr. Strange')