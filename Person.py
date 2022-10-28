class Person:
    def __init__(self, f_name, l_name, age):
        self.f_name = str(f_name)
        self.l_name = str(l_name)
        self.age = int(age)
    # since Person class is parent class nothing much is need to be said
    def do_work(self):
        print(f'{self.f_name} {self.l_name} is unemployed')
