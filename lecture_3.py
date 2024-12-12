stock_price = "1100"

# different ways to output the same things
print("Today's price for google stock is:", stock_price)
print("Today's price for google stock is: {}" .format(stock_price))
print(f"Today's price for google stock is: {stock_price}")

print(f"Today's price for google stock is: {4+5}")

today_price = "1100"
yesterday_price = "1200"

print(f"Today's price for google stock is: {today_price}, yesterday price is: {yesterday_price}")

# special chars
# \ escape char, escapes special char
# \n -> new line within a string
# \t -> adds a tab
print("My name is Emi Dashler and \nnot only do I know nothing but \nI also do nothing.")
print("My name is Emi Dashler and \n\tnot only do I know nothing but \n\t\tI also do nothing.")
print("My name is Emi Dashler and \\n not only do I know nothing but \n I also do nothing.")