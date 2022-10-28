from Person import Person


class Nurse(Person):
    def __init__(self, f_name, l_name, age, hospital, department):
        super().__init__(f_name, l_name, age)
        self.hospital = str(hospital)
        self.department = str(department)

    def do_work(self):
        print(f'Hospital: {self.hospital}\nDepartment: {self.department}')

    def __str__(self):
        return f'Name: {self.f_name} {self.l_name}\nAge: {self.age}'