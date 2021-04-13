# Medium post https://medium.com/fintechexplained/everything-about-python-from-beginner-to-advance-level-227d52ef32d2

# Declare and assign variables

my_first_variable = 1
my_second_variable = 2
my_third_variable = "Hello Me"
my_pointer_var = my_first_variable

# slicing
y = 'Abc'
ab = y[:2]
bc = y[1:]
a = y[:-2]
bc2 = y[-2:]


# functions with optional args = just add a default value to the argument 
def my_function(optional='default'):
    return f'optional param equals= {optional}'

# define a function that accepts any number of arguments 
def function_multi_arg(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)
    print(f"Result from lambda = {kwargs['lambda_fun'](2,3)}")

if __name__ == '__main__':
    #print(dir())
    #print(my_function())
    #print(my_function('asdf'))
    #print(my_function(optional='qwerty'))
    #function_multi_arg(1,2,3,'asdf', 39.0, named_param='mmmmm', lambda_fun=lambda x,y: x + y)
    print(f'my_first_variable == {str(my_first_variable)} | ID == {id(my_first_variable)}')
    print(f'my_second_variable == {str(my_second_variable)} | ID == {id(my_second_variable)}')
    print(f'my_third_variable == {str(my_third_variable)} | ID == {id(my_third_variable)}')
    print(f'my_pointer_var == {str(my_pointer_var)} | ID == {id(my_pointer_var)}')
    print('changing value of my_first_variable')
    my_first_variable = 'new value'
    print(f'NEW my_first_variable == {str(my_first_variable)} | ID == {id(my_first_variable)}')
    print(f'my_pointer_var == {str(my_pointer_var)} | ID == {id(my_pointer_var)}')
