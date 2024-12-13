my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
my_str_list = ["comp sci", "physics", " elec eng", "philosophy"]
my_new_list = ["art", "econ"]

print(f"Ints: {my_list}")
print(f"Strings: {my_str_list}")
'''my_list.sort() # method
sorted_list = sorted(my_list)
print(sorted_list) # fucntion

print("Sorting...")
print(f"Sorted Ints: {my_list}")

print("physics" in my_str_list)
print(50 in my_str_list)
print(my_str_list.index("physics"))
print(len(my_str_list))
print(my_list[-1])
print(my_list.count(15))'''

print("Add/remove...")

# append, insert(), extend()
my_list.append(25)
print(my_list)

# index, number
my_list.insert(5, 24)
print(my_list)

my_str_list.extend(my_new_list)
print(my_str_list)

# pop(), remove()
my_str_list.remove("comp sci")
print(my_str_list)

my_str_list.pop()
print(my_str_list)

print(my_list[-1])
my_list[-1] = 1000
print(my_list)
print(my_list[0:5])

for item in my_list:
    print(item)

# list comprehension is used to generate lists of items in 1 line in a clean, efficient manner
