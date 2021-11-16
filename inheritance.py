# inherit, extends, override

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")


class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        # calling the parent constructor
        # to fill name, and age infromation
        # for the SoftwareEngineer class
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging")

    # overriding the parent work method
    def work(self):
        print(f"{self.name} is <coding/>")


class Designer(Employee): 
    def draw(self):
        print(f"{self.name} is drawing")

    # overriding the parent work method
    def work(self):
        print(f"{self.name} is designing")


# because SoftwareEngineer inherits from Employee
# it should call it's constructor
se = SoftwareEngineer("ahmad", 22, 7000, "Junior")
se.debug()
se.work()

d = Designer("aliaa", 31, 8000)


d.draw()
d.work()
