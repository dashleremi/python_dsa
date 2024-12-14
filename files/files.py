# reading from and writing to files

file_name = 'data.txt'
with open(file_name) as f:
    for line in f:
        print(line.strip())

record_to_add = "joe, schmo:python,ruby,javascript"

with open(file_name, "a+") as to_write:
    to_write.write(record_to_add+"\n")