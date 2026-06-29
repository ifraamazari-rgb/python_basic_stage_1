class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def result(self):
        if self.marks >= 60:
            return "Pass"
        else:
            return "Fail"

student1 = Student("Ali", 20, 75)

print("Name:", student1.name)
print("Age:", student1.age)
print("Marks:", student1.marks)
print("Result:", student1.result())