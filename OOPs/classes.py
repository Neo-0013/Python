"""
Topic: Classes & Objects
Description: OOP basics — class, __init__, methods, self
"""

class Student:
    # Class variable
    school = "Python Academy"

    def __init__(self, name, grade):
        self.name = name      # instance variable
        self.grade = grade

    def introduce(self):
        return f"Hi, I'm {self.name} with grade {self.grade}"

    def __str__(self):
        return f"Student({self.name})"

# --- Creating Objects ---
s1 = Student("Neo", "A")
s2 = Student("John", "B")

print(s1.introduce())
print(s2)
print(Student.school)
