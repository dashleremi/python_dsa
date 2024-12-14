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

# objects, instances of class Student
courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']

emi = Student("emi", "dashler", courses_1)
john = Student("john", "munro", courses_2)

print(emi.first_name, emi.last_name, emi.courses)
print(john.first_name, john.last_name, john.courses)

emi.add_course("rails")
emi.add_course("java")
print(emi.first_name, emi.last_name, emi.courses)

john.remove_course("c")
john.remove_course("c")
john.remove_course("python")
print(john.first_name, john.last_name, john.courses)
