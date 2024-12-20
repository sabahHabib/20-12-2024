class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def display_details(self):
        return f"Name:{self.name} age:{self.age}"

class Student(Person):
    def __init__(self,name,age,std_id,grades=0):
        super().__init__(name,age)
        self.std_id=std_id
        self.__grades=grades

    def add_grade(self,x):
        self.__grades=x

    def get_grade(self):
        return f" {self.__grades}"

    def display_details(self):
        base_details=super().display_details()
        return f'{base_details} std_id:{self.std_id} grades:{self.__grades}'

class Teacher(Person):
    def __init__(self,name,age,teacher_id,course):
        super().__init__(name,age)
        self.teacher_id=teacher_id
        self.course=course
    def display_details(self):
        base_details=super().display_details()
        return f"{base_details} teacher id:{self.teacher_id} course:{self.course}"

class Course():
    def __init__(self,course_name,course_code):
        self.course_name=course_name
        self.course_code=course_code
        self.enrolled_student=[]
        self.assign_teacher=[]
    def add_student(self,student):
        if student not in self.enrolled_student:
            self.enrolled_student.append(student)
    def remove_student(self,student):
        if student in self.enrolled_student:
            self.enrolled_student.remove(student)

    def add_teacher(self,teacher):
        if teacher not in self.assign_teacher:
            self.assign_teacher.append(teacher)
    def remove_teacher(self,teacher):
        if teacher in self.assign_teacher:
            self.assign_teacher.remove(teacher)
    def display_details(self):
        student_name= [student.name for student in self.enrolled_student]
        teacher_name=[teacher.name for teacher in self.assign_teacher]
        return f"Enrolled courses:{self.course_name},course code:{self.course_code},Enrolled Student:{student_name},Assign Teachers:{teacher_name}"

std1=Student("ali",20,1)
std1.add_grade("A")
teacher1=Teacher("sana",30,1,"Math")
course1=Course("Math","001")
course1.add_teacher(teacher1)
course1.add_student(std1)
print(course1.display_details())
print(teacher1.display_details())
print(std1.display_details())

