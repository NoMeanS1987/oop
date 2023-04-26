class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self,lecturer,course,grade):
        if isinstance (lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __mid_value(self):
        return sum((list(self.grades.values()))[0])/len((list(self.grades.values()))[0])



    def __str__(self):
        return f'''Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за домашние задания: {self.__mid_value()} 
Курсы в процессе: {", ".join(self.courses_in_progress)} 
Завершенные курсы: {", ".join(self.finished_courses)}
'''

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):

    def __str__ (self):
        return f'''Имя: {self.name} 
Фамилия: {self.surname} 
Средняя оценка за лекции: {self.__mid_value()}   
        '''
    def __mid_value(self):
        return sum((list(self.grades.values()))[0]) / len((list(self.grades.values()))[0])

    def __lt__(self, other):
        if not isinstance(other,Lecturer):
            print('Not a Lecturer')
            return
        else:
            return self.__mid_value() < other.__mid_value()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__ (self):
        return f'''Имя: {self.name} 
Фамилия: {self.surname} 
        '''


best_student = Student('Morty', 'Smith', 'Male')
best_student.courses_in_progress += ['Python','Git']

worse_student = Student('Summer', 'Smith', 'Female')
worse_student.courses_in_progress +=['Python', 'Git']

rew = Reviewer('Ben', 'Franclin')
rew.courses_attached += ['Python']

rew2 = Reviewer('Barak', 'Obama')
rew2.courses_attached += ['Git']

lec3 = Lecturer('Dan','Brown')
lec3.courses_attached += ['Python']
lec = Lecturer('Rick', 'Sacnhez')
lec.courses_attached += ['Python']
lec2 = Lecturer('Cick', 'Canchez')
lec2.courses_attached +=['Git']

rew.rate_hw(best_student, 'Python', 10)
rew.rate_hw(best_student, 'Python', 10)
rew.rate_hw(best_student, 'Python', 10)
rew2.rate_hw(best_student, 'Git', 10)
rew2.rate_hw(best_student, 'Git', 10)
rew2.rate_hw(best_student, 'Git', 10)

rew.rate_hw(worse_student, 'Python', 2)
rew.rate_hw(worse_student, 'Python', 3)
rew.rate_hw(worse_student, 'Python', 1)
rew2.rate_hw(worse_student, 'Git', 3)
rew2.rate_hw(worse_student, 'Git', 1)
rew2.rate_hw(worse_student, 'Git', 4)

best_student.rate_lc(lec, 'Python', 9.99)
best_student.rate_lc(lec, 'Python', 9.99)
best_student.rate_lc(lec, 'Python', 9.99)
best_student.rate_lc(lec2, 'Git', 8)
best_student.rate_lc(lec2, 'Git', 6)
best_student.rate_lc(lec2, 'Git', 9.99)
best_student.rate_lc(lec3, 'Python', 5)
best_student.rate_lc(lec3, 'Python', 6)
best_student.rate_lc(lec3, 'Python', 8)

print(best_student.grades)
print(worse_student)
print(rew)
print(rew2)
print(lec.grades)
print(lec2)
print(lec < lec2)
print(lec2 < lec)

studlist = [best_student,worse_student]
leclist = [lec,lec3]
def studmidle(studlist,coursename):
    val = 0
    k = 0
    for i in range(len(list(studlist))):
        val += (sum(list(studlist[i].grades[coursename])))
        for course in studlist[i].grades[coursename]:
            k += 1
    print(val/k)

studmidle(studlist,"Python")

def lecmidle(leclist,course):
    val = 0
    k = 0
    for i in range(len(list(leclist))):
        val+=sum(list(leclist[i].grades[course]))
        for courses in leclist[i].grades[course]:
            k += 1
    print(val/k)

lecmidle(leclist,'Python')