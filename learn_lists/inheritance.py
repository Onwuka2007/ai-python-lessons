# both students and professors are wizard
# a student inherits from the super class (Wix=zard)


class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self):
        return f"{self.name} is just a wizard, no assigned role."


class Student(Wizard):
    def __init__(self, name, house):
        # inherit from the super (Wizard) and also its attributes (.__init__(name))
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} is a student in {self.house}."


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{self.name} teaches {self.subject}."


print(Wizard("Albus"))
print(Student("Harry", "Gryffindor"))
print(Professor("Severus", "Defense Against the Dark Arts"))
