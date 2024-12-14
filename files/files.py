# reading from and writing to files

file_name = 'data.txt'
emi = Student("emi", "dashler", ["python", "ruby", "javascript"])
print(emi.find_in_file(file_name))
print(emi.add_to_file(file_name))

joe = Student("joe", "schmo", ["python", "ruby", "javascript"])
print(joe.find_in_file(file_name))
print(joe.add_to_file(file_name))