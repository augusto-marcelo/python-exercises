import functools

def startstop(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished")
    return wrapper

# Measuring execution time 
def measure_time(func):
    def wrapper():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print(f"The time needed: {end_time - start_time} seconds")
    
    return wrapper

# Slowing code down
def sleep(func):
    def wrapper():
        time.sleep(5)
        return func() # execute & return the value of the inner function
        #func() # just execute
    return wrapper


def debug(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        func(*args, **kwargs)
        print(f'{func.__name__} completed')
    
    return wrapper

def do_twice(func):

    #Preserves the Introspecation ability of the inner function. If you don't use this, the
    # func.__name__ will be "funcion_wrapper"
    # in other words, this will preserve the metadata from original function at runtime
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return wrapper

def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper_repeat

    if _func is None: 
        return decorator_repeat
    else:
        return decorator_repeat(_func)