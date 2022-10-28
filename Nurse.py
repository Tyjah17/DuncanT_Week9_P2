from PersonII import PersonII


# child of parent class Person
class Nurse(PersonII):
    # Nurse Constructor
    def __init__(self, f_name, l_name, age, hospital, department):
        # Person Constructor
        super().__init__(f_name, l_name, age)
        # Nurse properties
        self.hospital = str(hospital)
        self.department = str(department)

    # print hospital that Nurse works at and what department they are in
    def do_work(self):
        print(f'Hospital: {self.hospital}\nDepartment: {self.department}')

    # string method that only displays name and age
    def __str__(self):
        return f'Name: {self.f_name} {self.l_name}\nAge: {self.age}'
