from Teacher import Teacher
from Programmer import Programmer
from Nurse import Nurse

if __name__ == '__main__':
    # list of people(Person) with occupations
    list_of_occupants = [Teacher('Nathan', 'Drake', 38, 'History', 3),
                         Teacher('Patricia', 'Smith', 69, 'Calculus II', 12),
                         Programmer('Tyjah', 'Duncan', 20, 'Software Developer', 'PyCharm'),
                         Programmer('Jackson', 'Whelan', 20, 'Web Developer', 'Eclipse'),
                         Nurse('Hunner', 'Ford', 20, 'North Suburban Medical Center', 'Anesthesiology'),
                         Nurse('Arthur', 'Morgan', 36, 'Centura St. Anthony North Hospital', 'Cardiology')]

    for obj in list_of_occupants:
        print(obj)
        obj.do_work()
        print("----------------------")
