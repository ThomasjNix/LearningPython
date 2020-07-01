from person import Person

# Inheritance makes it possible to extend existing functionality for finer organization of class structures

"""
Classes are defined with this syntax
the initializer function is used when constructing an instance of the class
all arguments beyond self are passed and can be used for assignment

A standard class is just class ClassName(), but a class to extend (in this case person) can be provided
When extending properties from a base class, be sure to make the super() call and call __init__() with the
necessary parameters needed to initialize the instance of the base class
"""
class Student(Person):
    def __init__(self, name, major, gpa):
        super().__init__(name)
        self.major = major
        self.gpa = gpa

    def get_description(self):
        print(self.name + " is a " + self.major + " major with a GPA of " + str(self.gpa) + ".")