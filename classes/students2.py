# first_name, last_name, courses

# class names = camel case, capitalize
class Student:
    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last

        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

    def __len__(self):
        return len(self.courses)
    
    def __repr__(self):
        # string representation, less used than __str__
        return f"Student('{self.first_name}', '{self.last_name}', '{self.courses}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"

# objects, instances of class Student
courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']

emi = Student("emi", "dashler", courses_1)
john = Student("john", "munro", courses_2)

print(emi)
print(repr(emi))
print(john)
print(repr(john))

# prints out all classes that can be used with emi
# includes the ones i custom made
'''
print(dir(emi))
print(emi.__dir__)
'''