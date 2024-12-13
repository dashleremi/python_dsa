my_set = {1, 6, 2, 'java', 'ruby', 8, 9, 10, 21, 1000, 'python'}
my_list = [1, 6, 2, 'java', 'ruby', 8, 9, 10, 21, 1000, 6, 'python', 'java']
programming_set = {'java', 'ruby', 'javascript', 'python', 'c'}


print(my_list)
my_set = set(my_set)
print(my_set) # unordered everytime

print('java' in my_set)

print(my_set.intersection(programming_set))
print(my_set.union(programming_set))
print(my_set.difference(programming_set))

for item in my_set:
    print(item)