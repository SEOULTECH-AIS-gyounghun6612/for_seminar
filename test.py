class Animal:
    def __init__(self, leg: int, tail: int, eye: int):
        self.leg = leg
        self.tail = tail
        self.eye = eye

    def get_atribute(self):
        return self.__dict__

class Person(Animal):
    def __init__(self, name: str, age: int):
        super(Person, self).__init__(leg=2, tail=0, eye=2)
        self.name = name
        self.age = age
    # get_atribute를 따로 선언하지 않아도 상속받은 get_atribute가 존재 함.


class Bird(Animal):
    def __init__(self, name: str, wing: int):
        super(Bird, self).__init__(leg=2, tail=0, eye=2)
        self.name = name
        self.wing = wing

    # get_atribute를 따로 선언하여 상속받은 get_atribute를 덮어쓰기 함.
    def get_atribute(self):
        atribute = {'name': self.name, 'wing': self.wing}
        atribute.update(super().__dict__)
        return atribute


if __name__ == "__main__":
    student01 = Person("sangmin", 28)
    chicken = Bird("chicken", 2)
    print(student01.get_atribute())

    print(chicken.get_atribute())
