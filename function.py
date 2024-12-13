# structure

'''def name_of_func():
       code to perform function operations must 
       be indented to be considered part of the function

'''

# functions may or may not contain parameters

# example 1 with parameters
def add_two_nums(num1, num2):
    # docstring
    """
    this functions add two numbers
    input: two integer values to add
    output: the sum of the two input integers
    """
    return num1 + num2

# example 2 without parameters
def say_hello():
    print("Hello World!")

# good practice to include a docstring in the function to provide informatino about it (optional)

def say_hello():
    '''this function prints hello world'''
    print('hello world')

# try to limit a function to perform onlny 1 defined function
# functions can return multiple values (tuples)
def ints_and_dict(some_parameters):
    """
    this function performs some operation
    and returns the integer list and a dictionary as output of the operation
    """
    return ints_list, custom_dict


