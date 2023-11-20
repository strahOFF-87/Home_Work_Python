class Human:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        # self.set_age(age)
        self.age = age

    @property
    # def get_age(self):
    def age(self):
        return self.__age

    @age.setter
    # def set_age(self, age: int):
    def age(self, age: int):
        if not isinstance(age, int):
            print("не число")
            self.__age = 0
        else:
            if age < 0:
                self.__age = 0
                print("возраст меньше 0")
            else:
                self.__age = age


Ivan = Human("Ivan", "Strakhov", 36)
# print(Ivan.get_age())
# Ivan.set_age(37)
# print(Ivan.get_age())
print(Ivan.age)
Ivan.age = 37
print(Ivan.age)
