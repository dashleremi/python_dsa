import string # importing ascii, etc from the documentation

message = "The price of the stock is:"
price = "$1200"

new_message = message + " " + price
print(new_message)

# id = memory location

# indexing
name = "Interstellar"
print(name[4])

# slicing
name_two = "challenging"
print(name_two[0:8])
print(name_two[:8])

# step sizing
nums = "1234567890"
print(nums[::2])
print(nums[::-1])

greeting = "hello"
user = "ashley"
message = "welcome to this course."
print(greeting.upper(), user.capitalize(), message.lower())
print(len(greeting))
# includes white space
print(len(message))
print(type(message))
print(id(message))
#print(dir(user))
print(message.find("course"))
print(message.split())