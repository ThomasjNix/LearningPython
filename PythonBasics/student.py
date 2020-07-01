"""
Classes are defined with this syntax
the initializer function is used when constructing an instance of the class
all arguments beyond self are passed and can be used for assignment
"""
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def get_description(self):
        print(self.name + " is a " + self.major + " major with a GPA of " + str(self.gpa) + ".")