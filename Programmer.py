from PersonII import PersonII


# child class of Person class
class Programmer(PersonII):
    # Programmer Constructor
    def __init__(self, f_name, l_name, age, specialty, preferred_ide):
        # Person Constructor
        super().__init__(f_name, l_name, age)
        # Programmer properties
        self.specialty = str(specialty)
        self.preferred_ide = str(preferred_ide)

    # print work specialty and preferred IDE
    def do_work(self):
        print(f'Specialty: {self.specialty}\nPreferred IDE: {self.preferred_ide}')
    # dunder str method that prints name and age
    def __str__(self):
        return f'Name: {self.f_name} {self.l_name}\nAge: {self.age}'
