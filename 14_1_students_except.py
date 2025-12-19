class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender} {self.age} {self.first_name} {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        super().__str__()
        return f"{self.gender} {self.age} {self.first_name} {self.last_name} {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise CustomerException(student)

    def delete_student(self, last_name):
        self.group = [s for s in self.group if s != self.find_student(last_name)]

    def find_student(self, last_name):
        for stud in self.group:
            if stud.last_name == last_name:
                return stud
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f"{student}\n"
        return f'Number:{self.number}\n{all_students}'

class CustomerException(Exception):

    def __init__(self, student, message="The group has only 10 students!"):
        self.student = student
        self.message = message
        super().__init__(self.message)

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 45, 'Marta', 'Johns', 'AN149')
st4 = Student('Male', 33, 'Steven', 'Johnson', 'AN141')
st5 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st7 = Student('Female', 45, 'Marta', 'Johns', 'AN149')
st8 = Student('Male', 33, 'Steven', 'Johnson', 'AN141')
st9 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st10 = Student('Female', 45, 'Marta', 'Johns', 'AN149')
st11 = Student('Male', 33, 'Steven', 'Johnson', 'AN141')

lst_of_students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]
gr_of_studs = Group('Group of students')

for stu in lst_of_students:
    try:
        gr_of_studs.add_student(stu)
        print(f"Student {stu} is added to {gr_of_studs.number}")
    except CustomerException as e:
        print(f"Mistake: {e}")
    except Exception as e:
        print(f"Another mistake: {e}")
