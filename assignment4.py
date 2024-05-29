class person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce (self):
        print(f'This is {self.name}. This person is {self.age} years old and is of {self.gender} gender.' )
a = person('Bilal', 25, 'Male')
a.introduce()
