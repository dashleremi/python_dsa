## Challenge exercise - list, tuple, dictionary and functions.
# Sample execution code is provided at the bottom, you may run it now
# to see and get a feel for the existing output then build each function
# and re-run the script.
from collections import Counter

# list_of_records
buckets = [ ('john.doe@example.com',{'first_name':'john','last_name':'doe'}),
            ('jane.doe@example.com',{'first_name':'jane','last_name':'doe'}),
            ('derek.zoo@example.com',{'first_name':'derek','last_name':'zoolander'}),
            ('murph.cooper@example.com',{'first_name':'murph','last_name':'cooper'}),
            ('ned.stark@example.com',{'first_name':'ned','last_name':'stark'})
            ]

# Question 1: Create a function that returns all last names in the list
# with the number of occurances of that last name, example 'doe': 2, 'stark': 1
# use the Counter function from collections module to count the occurances with ease.
def get_last_name_count(list_of_records):
    """
    fill in docstring
    """
    ## Write code below ##
    last_names = [record[1]['last_name'] for record in list_of_records]
    return Counter(last_names)

    ## end of function ##


# Question 2: Create a function that compares first and last names of records
# given the email address, first and last names to compare. Exact matches only,
# ignore case. Return True if exact match, return False otherwise.
def compare_full_name(list_of_records, email, first_name, last_name):
    """
    fill in docstring
    """
    ## Write code below ##
    for record in list_of_records:
        if record[0] == email:
            if (record[1]['first_name'].lower() == first_name.lower() and record[1]['last_name'].lower() == last_name.lower()):
                return True
    return False
    ## end of function ##

# (CHALLENGE) Question 3: Create a function that can reset the value for first_name
# and last_name for a record found with a specific email address
# while leaving the rest of the list unchanged, if the email address
# does not exist, then append a new record to the list with the new email
# address, first name and last name.
# Hint: Solutions use the enumerate function to track index of a record.
def update_record(list_of_records, email, first_name, last_name):
    """
    fill in docstring
    """
    ## Write code below ##
    for index, record in enumerate(list_of_records):
        if record[0] == email:
            list_of_records[index] = (email, {'first_name': first_name, 'last_name': last_name})
            return
        list_of_records.append((email, {'first_name': first_name, 'last_name': last_name}))
    ## end of function ##

def divider():
    print()
    print("-"*40)
    print()

print("The last names and their counts are as follows:")
result = get_last_name_count(buckets)
# un-comment the code below once your get_last_name_count function works
for k, v in result.items():
    print(f"{k}: {v}")
divider()

print("Does ned's first and last name match our records?")
print(compare_full_name(buckets,'ned.stark@example.com','ned','stark'))
divider()

print("Changing john's first name to jon and last name to snow")
update_record(buckets,'john.doe@example.com','jon','snow')
divider()

print("Adding new record ironman@example.com")
update_record(buckets,'ironman@example.com','iron','man')
divider()

print("Updated last names and their count are as follows:")
result = get_last_name_count(buckets)
# un-comment the code below once your get_last_name_count function works
for k, v in result.items():
    print(f"{k}: {v}")
divider()

print("Full list")
for item in buckets:
    record_email, full_name = item
    print(f"Email: {record_email}, first name: {full_name['first_name']}, last_name: {full_name['last_name']}")
