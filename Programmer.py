from Person import Person


class Programmer(Person):
    def __init__(self, f_name, l_name, age, specialty, preferred_ide):
        super().__init__(f_name, l_name, age)
        self.specialty = str(specialty)
        self.preferred_ide = str(preferred_ide)

    def do_work(self):
        print(f'Specialty: {self.specialty}\nPreferred IDE: {self.preferred_ide}')

    def __str__(self):
        return f'Name: {self.f_name} {self.l_name}\nAge: {self.age}'
