from random import randint
# while loops
# break and pass keyword
# generator - zip function

truth_condition = True

l1 = [randint(1, 1000) for num in range(1000)]
# i = 0
num_to_search = 25

'''while i < len(l1):
    if l1[i] == num_to_search:
        print(f"{num_to_search} found at index {i}")
        break
    i += 1'''

for index, num in enumerate(l1):
    if num == num_to_search:
        print(f"{num_to_search} found at index {index}")
        break