print("Welcome to the calc program")
print("-" * 30)

choice = input("Choose 1 to multiple, 2 to divide -> ")

'''if choice == "1":
    print(f"{num1} multiplied by {num2} is: {num1 * num2}")
elif choice == "2":
    print(f"{num1} divided by {num2} is: {num1 / num2}")
else:
    print("You've made an invalid selection")
'''

if choice == "1" or choice == "2":
    num1 = int(input("Enter first number -> "))
    num2 = int(input("Enter second number -> "))
    if choice == "1":
        print(f"{num1} multiplied by {num2} is: {num1 * num2}")
    else:
        print(f"{num1} divided by {num2} is: {num1 / num2}")
else:
    print("You've made an invalid selection")