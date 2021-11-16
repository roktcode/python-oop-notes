class SoftwareEngineer:
    def __init__(self):

        self._salary = None

    # getter property

    @property
    def salary(self):
        return self._salary

    # setter property

    @salary.setter
    def salary(self, value):
        self._salary = value

    # delete property

    @salary.deleter
    def salary(self):
        del self ._salary


se = SoftwareEngineer("Ahmad", 22)

se.salary = 6000
print(se.salary)

del se.salary
print(se.salary)
