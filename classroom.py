from students import Student
from teachers import Teacher

student_list=[]
teacher_list=[]

def addStudent(name,studentNumber,department):
    newStudent = Student(name,studentNumber,department)
    student_list.append(newStudent)

def addTeacher(name,teacherId,department):
    newTeacher = Teacher(name,teacherId,department)
    teacher_list.append(newTeacher)

def StudentList():
    for student in student_list:
        student.studentInfo()
        student.departmentInfo()
        print("---------------------------------------------------------")

def TeacherList():
    for teacher in teacher_list:
        teacher.teacherInfo()
        teacher.departmentInfo()
        print("---------------------------------------------------------")

addStudent("Emine",200,"Matematik")
addStudent("Gül",350,"Gazetecilik")

addTeacher("İrem",500,"Tobeto")
addTeacher("Mustafa",450,"Tobeto")

StudentList()
TeacherList()
