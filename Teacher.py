from Person import Person


class Teacher(Person):
    def __init__(self, f_name, l_name, age, subject, grade):
        super().__init__(f_name, l_name, age)
        self.subject = str(subject)
        self.grade = int(grade)

    def do_work(self):
        if self.grade == 1:
            print(f'Teaches: {self.grade}st grade {self.subject}')
        elif self.grade == 2:
            print(f'Teaches: {self.grade}nd grade {self.subject}')
        elif self.grade == 3:
            print(f'Teaches: {self.grade}rd grade {self.subject}')
        else:
            print(f'Teaches: {self.grade}th grade {self.subject}')

    def __str__(self):
        return f'Name: {self.f_name} {self.l_name}\nAge: {self.age}'
