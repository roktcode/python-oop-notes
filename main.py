# software engineer

se1 = ["Software Engineer", "Ahamd", 22, "Senior Developer", 5500]
se22 = ["Software Engineer", "Manal", 45, "Junior Engineer", 7000]


class SoftwareEngineer:

    # class attribute
    alias = "Keyboard magician"

    # initlaize the new instance
    def __init__(self, name, age, level, salary):
        # instance atributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    # self is auto given to methods
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # dunder method (special built-in methods thatcan  be overidden)
    def __str__(self):
        info = f"name={self.name}, age={self.age} level={self.level}"
        return info

    # compares two objects
    # example: se1 == se2
    # here, se1 is self, se2 is other
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # if we remove self,
    # method should be called as class method
    # like: SoftwareEngineer.entry_salary(30)
    @staticmethod
    def entry_salary(age):
        if age <= 25:
            return 5000
        elif age <= 40:
            return 6000
        else:
            return 7000


se1 = SoftwareEngineer("Ahmad", 22, "Senior", 6000)
se2 = SoftwareEngineer("Aliaa",  21, "Senior", 4400)
se3 = SoftwareEngineer("Aliaa",  20, "Senior", 4400)

# print(se2 == se3)

# print(se1.entry_salary(30))
print(se1.entry_salary(30))
