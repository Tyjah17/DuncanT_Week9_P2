# parent class for Teacher, Programmer, and Nurse
class PersonII:
    def __init__(self, f_name, l_name, age):
        self.f_name = str(f_name)
        self.l_name = str(l_name)
        self.age = int(age)

    # Person class is parent and doesn't have any tasks so display unemployed for now
    def do_work(self):
        print(f'{self.f_name} {self.l_name} is unemployed')
