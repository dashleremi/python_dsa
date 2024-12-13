my_random_tuple = ('first', 1, 7, 6, 4, 5, 8, 'hi there', 2, 3, 1, 5, 2, 1, 9, 10)
my_tuple = ('first_value', 'second_value', 'third_value')

'''print(my_random_tuple)
print(my_random_tuple[0])

print(dir(my_random_tuple)) # functions able to use
print(my_random_tuple.index('hi there'))'''

first_var, second_var, third_var = my_tuple
print(third_var)
print('first' in my_random_tuple)

for item in my_random_tuple:
    print(item)