from student import Student
from school import School

exampleStudent1 = Student("Mike", "Biology", 3.5)
exampleStudent2 = Student("Jim", "Mathematics", 4.0)
exampleStudent3 = Student("Catherine", "Computer Science", 2.7)
exampleStudent4 = Student("Joseph", "Law", 2.2)
exampleStudent5 = Student("Angel", "Environmental Sciences", 3.2)

exampleSchool = School("Example University", "Somewhere, Wisconsin", [exampleStudent1, exampleStudent2, exampleStudent3, exampleStudent4, exampleStudent5])

exampleSchool.get_school_details()
exampleSchool.get_all_student_descriptions()