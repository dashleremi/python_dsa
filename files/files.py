# reading from and writing to files

file_name = 'data.txt'

# function to convert string to parameters for __init__
def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(",")
    course_details = line[1].rstrip().split(",")
    return first_name, last_name, course_details

# function to convert Student object to string for write to file
def prep_to_write(first_name, last_name, courses):
    full_name = first_name + " " + last_name
    courses = ",".join(courses)
    return full_name + ":" + courses

with open(file_name) as f:
    for line in f:
        print(line.strip())
        first_name, last_name, course_details = prep_record(line)
        print(first_name, last_name, course_details)

to_write = prep_to_write(first_name, last_name, course_details)
print(to_write)
record_to_add = "joe,schmo:python,ruby,javascript"

# with open(file_name, "a+") as to_write:
    # to_write.write(record_to_add+"\n")