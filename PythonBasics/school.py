class School:
    def __init__(self, name, location, students):
        self.name = name
        self.location = location
        self.students = students

    def get_school_details(self):
        print(self.name + " is a university in " + self.location)
        print(self.name + " has a total of " + str(len(self.students)) + " students with an average GPA of " + str(round(self.get_students_gpa_average(), 2)))

    def get_students_gpa_average(self):
        totalGpa = 0
        for student in self.students:
            totalGpa += student.gpa
        return (totalGpa / len(self.students))

    def get_all_student_descriptions(self):
        print("The students enrolled at " + self.name + " are as follows:")
        for student in self.students:
            student.get_description()