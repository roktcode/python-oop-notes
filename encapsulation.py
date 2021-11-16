# hide attributes and provide
# getters and setters to access/modify them

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # convention to declare "protected" attributes
        # they are accesssbile though (use __to hide them "private")

        self._salary = None
        self._num_of_bugs_solved = 0

    def code(self):
        self._num_of_bugs_solved += 1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):
        self._salary = self._calc_salary(base_value)

    def _calc_salary(self, base_value):
        if self._num_of_bugs_solved < 10:
            return base_value
        elif self._num_of_bugs_solved < 100:
            return base_value * 2
        else:
            return base_value * 3


se = SoftwareEngineer("Ahmad", 22)

for i in range (100):
    se.code()

se.set_salary(6000)
print(se.get_salary())