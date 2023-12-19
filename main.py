class Human:
    name: str
    age: int
    passport: str

    def __init__(self, name: str, age: int, passport: str) -> None:
        self.name = name
        self.age = age
        self.passport = passport

    def get_info(self) -> list:
        return [self.name, self.age, self.passport]


class Student(Human):
    course: int
    scholar_ship: float
    group: str

    def __init__(self, name, age, passport, course, scholar_ship, group):
        super().__init__(name, age, passport)
        self.course = course
        self.scholar_ship = scholar_ship
        self.group = group

    def get_info(self) -> list:
        return super().get_info() + [self.course, self.scholar_ship, self.group]


stu = Student('Jane', 18, 'AD7777770', 1, 399.99, 'IFP23-01')
print(*stu.get_info())
