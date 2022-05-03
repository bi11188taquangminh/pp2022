class Student:
    def __init__(self):
        self.name = 'none'
        self.id = 'none'
        self.dob = ()
        self.list_courses = []


    def get_name (self):
        return self.name

    def get_id (self):
        return self.id

    def get_dob(self):
        return self.dob

    def get_courses(self):
        return self.courses 

    def set_student(self,x,y,a,b,c):
        self.id= x.lower()
        self.name = y.lower()
        self.dob = (a,b,c)

    def get_list_courses(self):
        return self.list_courses

    def add_courses (self,x,y):
        self.list_courses.append((x.lower(),y.lower(),-1))

    def remove_course (self,x):
        for course in self.list_courses:
            if course[0] == x.lower():
                self.list_courses.remove(course)

    def set_mark(self, course_id, mark):
        for course in self.list_courses:
            if course [0] == course_id:
                self.list_courses[2] = mark 

    def display_student_courses_list(self):
        print("mark = -1 means no information yet\n")
        print ("this student (course,id,mark) are: ")
        print(self.get_list_courses())

list_student = []

def add_student():
    a = Student()
    x= input("please enter id\t")
    y = input("please enter name\t")
    z= input ("please enter day of birth\t")
    m = input("please enter month of birth\t")
    n = input("please enter year of birth\t")
    a.set_student(y,x,z,m,n)
    list_student.append(a)
    

def display_student_infor(x):
    
    for student in list_student:
        if student.get_id() == x:
            print (f"this student name is {student.get_name()} with \
                id {student.get_id()}\n")
            print (f"the date of birth is {student.get_dob()[0]}/\
                {student.get_dob()[1]}/{student.get_dob()[2]}\n")

def search_student(x):
    for student in list_student:
        if student.get_id() == x:
            return student


def display_student_list():
    for student in list_student:
        print ("here is all students:\n")
        print (f"{student.get_name()}-{student.get_id()}\n")


while True:
    print("Choose one option by typing:\n" \
                "\t1. Add a student to Student List\n" \
                "\t2. Display a student information\n" \
                "\t3. Add a course to a student curriculum\n" \
                "\t4. Show all courses a student takes\n" \
                "\t5. Show all students in student list\n" \
                "\t6. Update mark of some student\n" \
                "\t7. Remove a student's course\n"\
                "\t8. Close program\n"
                "Input: " )
    choice = int(input())
    if choice == 8:
        break
    elif choice == 1:
        add_student()
    elif choice == 2:
        x = input("Please type the precise student id\t") 
        display_student_infor(x)
    elif choice == 3:
        x = input("Please type the precise student id\t")
        y = search_student(x)
        z = input ("Please type course id\t")
        m= input("Please type course name\t")
        y.add_courses(z,m)
    elif choice == 4:
        x = input("Please type the precise student id\t")
        y = search_student(x)
        y.display_student_courses_list()
    elif choice ==5:
        display_student_list()
    elif choice == 6:
        x = input("Please type the precise student id\t")
        y = search_student(x)
        m = input("enter the precise course id please\t")
        z = input("please enter mark of that subject\t")
        y.set_mark(m,z)
    elif choice == 7:
        x = input("Please type the precise student id\t")
        y = search_student(x)
        m = input("enter the precise course id please\t")
        y.remove_course(m)
